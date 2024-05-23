# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from thousandeyes_sdk.dashboards.models.api_widget_data_response import ApiWidgetDataResponse

class TestApiWidgetDataResponse(unittest.TestCase):
    """ApiWidgetDataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiWidgetDataResponse:
        """Test ApiWidgetDataResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiWidgetDataResponse`
        """
        model = ApiWidgetDataResponse()
        if include_optional:
            return ApiWidgetDataResponse(
                group_labels = [
                    thousandeyes_sdk.dashboards.models.api_report_data_component_label_map.ApiReportDataComponentLabelMap(
                        group_property = 'AGENT', )
                    ],
                bin_size = 3600,
                data = thousandeyes_sdk.dashboards.models.api_widgets_data_v2.ApiWidgetsDataV2(
                    cards = [
                        thousandeyes_sdk.dashboards.models.api_numbers_card_data.ApiNumbersCardData(
                            card_id = 'lrxxr', 
                            start_date = '2023-05-16T10:14:28Z', 
                            end_date = '2023-05-16T10:14:28Z', 
                            previous_value = 500.0, 
                            bin_size = 3600, 
                            timestamp = 1567620000, 
                            number_of_data_points = 24192, 
                            value = 100.0, 
                            status = 'No data', 
                            alert_suppression_windows = [
                                thousandeyes_sdk.dashboards.models.api_dashboard_asw.ApiDashboardAsw(
                                    id = '281474976710662', 
                                    name = 'Test dashboards', 
                                    test_ids = ["281474976710661"], 
                                    start_times = ["2023-05-16T10:14:28Z"], 
                                    duration_in_seconds = 7200, 
                                    repeat = 'custom', 
                                    repeat_every = 5, 
                                    repeat_unit = 'week', )
                                ], )
                        ], 
                    columns = [
                        thousandeyes_sdk.dashboards.models.api_multi_metric_column_data.ApiMultiMetricColumnData(
                            column_id = '938to', 
                            bin_size = 3600, 
                            points = [
                                thousandeyes_sdk.dashboards.models.api_widget_data_point.ApiWidgetDataPoint(
                                    timestamp = 1567620000, 
                                    number_of_data_points = 23304, 
                                    value = 100.0, 
                                    groups = [
                                        thousandeyes_sdk.dashboards.models.api_data_point_group.ApiDataPointGroup(
                                            group_property = 'COUNTRY', 
                                            group_value = 'US', )
                                        ], )
                                ], 
                            status = 'No data', )
                        ], 
                    points = [
                        thousandeyes_sdk.dashboards.models.api_widget_data_point.ApiWidgetDataPoint(
                            timestamp = 1567620000, 
                            number_of_data_points = 23304, 
                            value = 100.0, )
                        ], 
                    tests = [
                        thousandeyes_sdk.dashboards.models.api_test_table_data.ApiTestTableData(
                            test_id = '68256', 
                            test_name = 'Http Test Name', 
                            target = 'www.google.com', 
                            test_type = 'Web - HTTP Server', 
                            alert_count = 398, 
                            is_shared = True, 
                            graphlets = [
                                thousandeyes_sdk.dashboards.models.api_test_table_graphlets_data.ApiTestTableGraphletsData(
                                    metric = 'Availability', 
                                    test_id = '68257', )
                                ], )
                        ], 
                    start_round = 1384309800, 
                    alert_suppression_windows = [
                        thousandeyes_sdk.dashboards.models.api_dashboard_asw.ApiDashboardAsw(
                            id = '281474976710662', 
                            name = 'Test dashboards', 
                            test_ids = ["281474976710661"], 
                            start_times = ["2023-05-16T10:14:28Z"], 
                            duration_in_seconds = 7200, 
                            repeat_every = 5, )
                        ], 
                    total_alerts = 500, 
                    active_alerts = 483, 
                    alerts = [
                        thousandeyes_sdk.dashboards.models.api_alert_list_alert.ApiAlertListAlert(
                            alert_id = '2004945', 
                            test_id = '56512', 
                            rule_id = '281724', 
                            alert_source = 'Http Test', 
                            alert_rule = 'Http Test Rule', 
                            alert_type = 'network-end-to-end-server', 
                            start_time = '2023-06-02T08:54Z', 
                            duration_in_seconds = 25, 
                            active = True, )
                        ], 
                    summary = thousandeyes_sdk.dashboards.models.api_agent_status_summary.ApiAgentStatusSummary(
                        online = 10, 
                        offline = 2, 
                        disabled = 3, ), 
                    agents = [
                        thousandeyes_sdk.dashboards.models.api_agent_status_agent.ApiAgentStatusAgent(
                            agent_id = '6522', 
                            status = 'online', 
                            ip_info = thousandeyes_sdk.dashboards.models.api_agent_status_ip_info.ApiAgentStatusIpInfo(
                                public_ip = '172.58.92.31', 
                                private_ip = '172.58.92.31', 
                                ipv6 = '', 
                                operative_system_version = '', ), 
                            agent_name = '0c3898000117', 
                            location = thousandeyes_sdk.dashboards.models.api_agent_location.ApiAgentLocation(
                                latitude = 37.77493, 
                                longitude = -122.41942, 
                                location_name = 'San Francisco, California, US', ), )
                        ], 
                    status = 'No data', ),
                start_date = '2022-07-17T22:00:54Z',
                end_date = '2022-07-18T22:00:54Z',
                links = thousandeyes_sdk.dashboards.models.pagination_links.PaginationLinks(
                    previous = thousandeyes_sdk.dashboards.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    next = thousandeyes_sdk.dashboards.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    self = , )
            )
        else:
            return ApiWidgetDataResponse(
        )
        """

    def testApiWidgetDataResponse(self):
        """Test ApiWidgetDataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
