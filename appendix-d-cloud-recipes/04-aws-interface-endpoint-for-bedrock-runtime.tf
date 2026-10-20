resource "aws_vpc_endpoint" "bedrock_runtime" {
  vpc_id              = aws_vpc.ai.id
  service_name        = "com.amazonaws.${var.region}.bedrock-runtime"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = aws_subnet.ai_private[*].id
  security_group_ids  = [aws_security_group.bedrock_endpoint.id]
  private_dns_enabled = true
  tags = { service = "ai-platform", data_class = "confidential" }
}
