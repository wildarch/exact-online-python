import re
from datetime import date as Date
from urllib import parse

import authenticator
from swagger_client import ApiClient, DefaultApi

edm_datetime_regex = re.compile(r'/Date\((\d*)\)/')


def get_skiptoken(d):
    url = d.next
    parsed = parse.urlparse(url)
    try:
        return parse.parse_qs(parsed.query)['$skiptoken'][0]
    except KeyError:
        pass #No skiptoken


def format_date(date):
    formatted = date.isoformat()
    return '{0}'.format(formatted)


def format_dates(item):
    if item.start_date is not None:
        item.start_date = format_date(item.start_date)
    if item.end_date is not None:
        item.end_date = format_date(item.end_date)
    return item


def parse_date(date_str):
    parsed = re.match(edm_datetime_regex, date_str)
    if parsed is None:
        raise ValueError("Could not convert {0} to date".format(date_str))
    stamp = int(parsed.group(1))
    return Date.fromtimestamp(stamp/1000)


def parse_dates(item):
    if item.start_date is not None:
        item.start_date = parse_date(item.start_date)
    if item.end_date is not None:
        item.end_date = parse_date(item.end_date)
    return item


class Exact:
    def __init__(self, access_token=None, division=None, client_id=None, redirect_uri=None, secret=None):
        self.client = DefaultApi(ApiClient())

        if access_token is None:
            self.access_token = authenticator.get_token(client_id, redirect_uri, secret)
        else:
            self.access_token = access_token

        if division is None:
            self.division = self.current_division

    @property
    def current_division(self):
        me = self.client.get_me(self.access_token)
        return me.d.results[0].current_division

    """
        LOGISTICS
    """

    """
    Items
    """
    def get_items(self, **kwargs):
        res = self.client.division_logistics_items_get(self.division, self.access_token, **kwargs)
        items = res.d.results
        while res.d.next is not None:
            skiptoken = get_skiptoken(res.d)
            res = self.client.division_logistics_items_get(self.division, self.access_token, skiptoken=skiptoken, **kwargs)
            items += res.d.results
        return list(map(parse_dates, items))

    def get_item_price(self, item, **kwargs):
        res = self.client.division_logistics_sales_item_prices_get(
            self.division,
            self.access_token,
            filter="Item eq guid'{0}'".format(item.id),
            top=1,
            **kwargs)
        if res.d.results is not None:
            return res.d.results[0]
        else:
            return None

    def post_item(self, item, **kwargs):
        item = format_dates(item)
        self.client.division_logistics_items_post(self.division, self.access_token, item, **kwargs)

    def put_item(self, item):
        item = format_dates(item)
        item_id = "'{0}'".format(item.id) # Surround with single quotes
        item.id = None # Items should have their ID removed before PUTting
        self.client.division_logistics_items_guiditem_id_put(self.division, item_id, self.access_token, item)

    def delete_item(self, item_id):
        item_id = "'{0}'".format(item_id)
        self.client.division_logistics_items_guiditem_id_delete(self.division, item_id, self.access_token)

    """
    Item Groups
    """
    def get_item_groups(self, **kwargs):
        return self.client.division_logistics_item_groups_get(self.division, self.access_token,**kwargs).d.results

    """
        PAYROLL
    """
    """
    Employees
    """
    def get_employees(self, **kwargs):
        res = self.client.division_payroll_employees_get(self.division, self.access_token, **kwargs)
        employees = res.d.results
        while hasattr(res.d, 'next') and res.d.next is not None:
            skiptoken = get_skiptoken(res.d)
            res = self.client.division_payroll_employees_get(self.division, self.access_token, skiptoken=skiptoken,
                                                             **kwargs)
            employees += res.d.results
        return employees

    """
    EmployeeContracts
    """
    def get_employee_contracts(self, **kwargs):
        res = self.client.division_payroll_employment_contracts_get(self.division, self.access_token, **kwargs)
        employees = res.d.results
        while hasattr(res.d, 'next') and res.d.next is not None:
            skiptoken = get_skiptoken(res.d)
            res = self.client.division_payroll_employment_contracts_get(self.division, self.access_token, skiptoken=skiptoken,
                                                                        **kwargs)
            employees += res.d.results
        return employees

    """
        MANUFACTURING
    """
    """
    ShopOrders
    """
    def get_shop_orders(self, **kwargs):
        res = self.client.division_manufacturing_shop_orders_get(self.division, self.access_token, **kwargs)
        shop_orders = res.d.results
        while hasattr(res.d, 'next') and res.d.next is not None:
            skiptoken = get_skiptoken(res.d)
            res = self.client.division_manufacturing_shop_orders_get(self.division, self.access_token, skiptoken=skiptoken, **kwargs)
            shop_orders += res.d.results
        return shop_orders
    """
    ShopOrderRoutingStepPlans
    """
    def get_shop_order_routing_step_plans(self, **kwargs):
        res = self.client.division_manufacturing_shop_order_routing_step_plans_get(self.division, self.access_token, **kwargs)
        plans = res.d.results
        while hasattr(res.d, 'next') and res.d.next is not None:
            skiptoken = get_skiptoken(res.d)
            res = self.client.division_manufacturing_shop_order_routing_step_plans_get(self.division, self.access_token, skiptoken=skiptoken, **kwargs)
            plans += res.d.results
        return plans
    """
    TimeTransactions
    """
    def post_time_transaction(self, transaction, **kwargs):
        self.client.division_manufacturing_time_transactions_post(self.division, self.access_token, transaction, **kwargs)

    """
        DOCUMENTS
    """
    """
    DocumentAttachments
    """
    def get_document_attachments(self, **kwargs):
        res = self.client.division_documents_document_attachments_get(self.division, self.access_token, **kwargs)
        attachments = res.d.results
        while hasattr(res.d, 'next') and res.d.next is not None:
            skiptoken = get_skiptoken(res.d)
            res = self.client.division_documents_document_attachments_get(self.division, self.access_token, skiptoken=skiptoken, **kwargs)
            attachments += res.d.results
        return attachments
    """
    Documents
    """
    def get_documents(self, **kwargs):
        res = self.client.division_documents_documents_get(self.division, self.access_token, **kwargs)
        documents = res.d.results
        while hasattr(res.d, 'next') and res.d.next is not None:
            skiptoken = get_skiptoken(res.d)
            res = self.client.division_documents_documents_get(self.division, self.access_token, skiptoken=skiptoken, **kwargs)
            documents += res.d.results
        return documents

    """
        PROJECTS
    """
    """
    Projects
    """
    def get_projects(self, **kwargs):
        res = self.client.division_project_projects_get(self.division, self.access_token, **kwargs)
        projects = res.d.results
        while hasattr(res.d, 'next') and res.d.next is not None:
            skiptoken = get_skiptoken(res.d)
            res = self.client.division_manufacturing_shop_orders_get(self.division, self.access_token, skiptoken=skiptoken, **kwargs)
            projects += res.d.results
        return projects
