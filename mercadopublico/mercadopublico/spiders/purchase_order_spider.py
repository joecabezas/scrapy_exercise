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
        print('>>>' + response.xpath('//*[@id="rptResultados_ctl01_lblNombre"]').get())
