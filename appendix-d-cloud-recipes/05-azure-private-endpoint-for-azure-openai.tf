resource "azurerm_private_endpoint" "aoai" {
  name                = "pe-aoai-assistant"
  location            = azurerm_resource_group.ai.location
  resource_group_name = azurerm_resource_group.ai.name
  subnet_id           = azurerm_subnet.private_endpoints.id

  private_service_connection {
    name                           = "aoai-connection"
    private_connection_resource_id = azurerm_cognitive_account.aoai.id
    subresource_names              = ["account"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name                 = "aoai-dns"
    private_dns_zone_ids = [azurerm_private_dns_zone.openai.id]
  }
}
