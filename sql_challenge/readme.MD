## Diagrama Entidad Relación

**Category**: Contiene las categorías de productos disponibles en el sitio de ecommerce. Cada categoría tiene un ID y un nombre.

**Item**: Contiene los productos o ítems disponibles para la venta. Cada ítem pertenece a una categoría y está asociado a un vendedor.

**ItemPrice**: Almacena el precio actual de cada ítem. Un ítem puede tener múltiples precios a lo largo del tiempo.

**ItemPriceHistory**: Registra el historial de precios de cada ítem. Permite consultar precios anteriores.

**Customer**: Contiene los datos de clientes del sitio de ecommerce. Pueden ser compradores o vendedores.

**Seller**: Contiene los datos de los vendedores, que son también clientes. Cada vendedor está asociado a un cliente.

**Buyer**: Contiene los datos de los compradores, que son también clientes. Cada comprador está asociado a un cliente.

**PurchaseOrder**: Registra los pedidos de compra realizados por los clientes. Contiene datos como el comprador, la fecha del pedido y el monto total del pedido.

**PurchaseOrderItem**: Almacena los detalles de cada ítem incluido en un pedido de compra. Permite consultar fácilmente qué se compró en cada pedido y la cantidad de cada ítem.

* Category y Item definen el catálogo de productos disponibles. 
* ItemPrice e ItemPriceHistory registran los precios de los productos. 
* Customer, Seller y Buyer contienen los datos de los clientes, que pueden ser compradores o vendedores. 
* PurchaseOrder y PurchaseOrderItem almacenan el historial de pedidos realizados, incluyendo los detalles de cada ítem en los pedidos.

Nota sobre el nombre de la tabla "PurchaseOrder": Si bien el desafío solicitaba que la tabla de órdenes fuese nombrada como Order, tal palabra es una palabra reservada de SQL. Podría haberla usado encerrandola en comillas o usando un prefijo. En este caso usamos el prefijo Purchase, dando nombre a la tabla PurchaseOrder, lo cual evita el problema.