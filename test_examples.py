import pytest
import get_csv_data as csv
import http_request as req
import assert_data as ass


class TestCls:
    csv_data = csv.CsvReader().get_csv_data("./data/csv_data.csv")

    # print(csv_data)
    def setup_class(cls):
        pass

    def teardown_class(cls):
        pass

    @pytest.mark.parametrize("test_data", csv_data)
    def test_1(self, test_data):
        print("start test")
        print(test_data[0], test_data[3], test_data[4], test_data[7])
        res = req.ApiRequest().send_request(method=test_data[3], url=test_data[4])
        print(res.status_code)
        # print(res.status_code==int(test_data[7]))
        assert ass.AssertRes.assert_result(code=int(res.status_code), status_code=int(test_data[7]))


if __name__ == '__main__':
    pytest.main()
