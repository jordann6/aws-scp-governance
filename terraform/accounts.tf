resource "aws_organizations_account" "sandbox" {
  name      = "sandbox"
  email     = replace(var.org_email_domain, "@", "+sandbox@")
  parent_id = aws_organizations_organizational_unit.sandbox.id

  role_name = "OrganizationAccountAccessRole"

  close_on_deletion = true

  lifecycle {
    ignore_changes = [role_name]
  }
}

resource "aws_organizations_account" "dev" {
  name      = "dev"
  email     = replace(var.org_email_domain, "@", "+dev@")
  parent_id = aws_organizations_organizational_unit.dev.id

  role_name = "OrganizationAccountAccessRole"

  close_on_deletion = true

  lifecycle {
    ignore_changes = [role_name]
  }
}

resource "aws_organizations_account" "prod" {
  name      = "prod"
  email     = replace(var.org_email_domain, "@", "+prod@")
  parent_id = aws_organizations_organizational_unit.prod.id

  role_name = "OrganizationAccountAccessRole"

  close_on_deletion = true

  lifecycle {
    ignore_changes = [role_name]
  }
}
