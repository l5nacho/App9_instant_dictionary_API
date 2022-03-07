import justpy as jp

class Doc:

    @classmethod
    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes='bg-gray-200 h-screen p-2')
        jp.Div(a=div, text='Definition API', classes='text-4xl m-2')
        jp.Hr(a=div)
        jp.Div(a=div, text='www.exaple.com/api?w=apple', classes='text-lg')
        jp.Hr(a=div)
        jp.Div(a=div, text='{"word": "apple", "definition": ["A native Eurasian tree of the genus ''Malus''.", '
                           '"The popular, crisp, round fruit of the apple tree, usually with red, yellow or green skin, '
                           'light-coloured flesh and pips inside.", "The wood of the apple tree."]}')
        return wp
