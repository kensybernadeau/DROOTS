from flask import jsonify

from dao.request import requestDAO
from dao.resources import ResourcesDAO
from handler.Request import RequestHandler
from handler.resources import ResourcesHandler


class StatisticsHandler:

    def build_statistic_dict(self, list):
        result = {}
        result['request_amount'] = list[0]
        result['resource_amount'] = list[1]
        return result

    def searchStatistics(self, args):
        week = args.get("week")
        day = args.get("day")
        statistic_list = []
        if (len(args) == 1) and week:
            statistic_list = RequestHandler().get_request_weekly_statistics(week)
            statistic_list.extend(ResourcesHandler().get_resource_weekly_statistics(week))
        elif (len(args) == 1) and day:
            statistic_list = RequestHandler().get_request_daily_statistics(day)
            statistic_list.extend(ResourcesHandler().get_resource_daily_statistics(day))
        else:
            return jsonify(Error="Malformed query string"), 400
        # result_list = []
        # for row in request_list:
        #     result = self.build_statistic_dict(row)
        #     result_list.append(result)
        return jsonify(Request=statistic_list)
