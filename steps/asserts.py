from radish import pick


@pick
class asserts:
    @staticmethod
    def contains(expression, text):
        assert expression in text, "'{}' not in '{}'".format(expression, text)
