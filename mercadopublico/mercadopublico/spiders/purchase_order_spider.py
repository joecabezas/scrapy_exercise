import scrapy

class PurchaseOrderSpider(scrapy.Spider):

    URL_SEARCH = "http://www.mercadopublico.cl/Portal/Modules/Site/Busquedas/BuscadorAvanzado.aspx?qs=2"
    URL_RESULTS = "http://www.mercadopublico.cl/Portal/Modules/Site/Busquedas/ResultadoBusqueda.aspx?qs=2"

    start_urls = [URL_SEARCH]

    name = "purchase_order"

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            url = self.URL_SEARCH,
            formdata = {
                'txtSearch':'2069-2137-cm19',
                'btnBusqueda.x':'37',
                'btnBusqueda.y':'8'
            },
            callback = self.get_results
        )

    def get_results(self, response):
        order_selectors = response.xpath('//tr[contains(@class, "cssGridAdvancedSearch")]/td[1]/a/@onclick')
        results = []
        for order_selector in order_selectors:
            order_relative_url = order_selector.re(r"open\('(.+?)'")[0]
            order_absolute_url = response.urljoin(order_relative_url)
            results.append(order_absolute_url)
        yield {"links":results}
