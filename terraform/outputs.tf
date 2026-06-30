output "organization_id" {
  value = aws_organizations_organization.org.id
}

output "organization_root_id" {
  value = aws_organizations_organization.org.roots[0].id
}

output "management_account_id" {
  value = aws_organizations_organization.org.master_account_id
}

output "sandbox_ou_id" {
  value = aws_organizations_organizational_unit.sandbox.id
}

output "workloads_ou_id" {
  value = aws_organizations_organizational_unit.workloads.id
}

output "dev_ou_id" {
  value = aws_organizations_organizational_unit.dev.id
}

output "prod_ou_id" {
  value = aws_organizations_organizational_unit.prod.id
}

output "sandbox_account_id" {
  value = aws_organizations_account.sandbox.id
}

output "dev_account_id" {
  value = aws_organizations_account.dev.id
}

output "prod_account_id" {
  value = aws_organizations_account.prod.id
}
