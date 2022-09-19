class AssertRes:
    @staticmethod
    def assert_result(code, status_code, data=None, result_data=None):
        if code and status_code:
            try:
                assert code == status_code
                if data and result_data:
                    assert data in result_data
                print("验证通过")
            except AssertionError as e:
                print("验证失败")
                return False
            return True
