from diagrams import Diagram, Cluster, Edge
from diagrams.aws.management import (
    Organizations,
    OrganizationsAccount,
    OrganizationsOrganizationalUnit,
)
from diagrams.aws.security import IAMPermissions

graph_attrs = {
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.8",
    "ranksep": "1.0",
    "nodesep": "0.4",
    "splines": "ortho",
}

node_attrs = {
    "fontsize": "10",
}

edge_attrs = {
    "fontsize": "9",
}

with Diagram(
    "AWS Organization SCP Governance",
    filename="docs/architecture",
    outformat="png",
    show=False,
    direction="TB",
    graph_attr=graph_attrs,
    node_attr=node_attrs,
    edge_attr=edge_attrs,
):
    root = Organizations("Organization\nRoot")

    with Cluster("Root-Level SCPs", graph_attr={"style": "dashed", "color": "firebrick", "fontcolor": "firebrick"}):
        scp_leave = IAMPermissions("deny-leave-org")
        scp_root_user = IAMPermissions("deny-root-user")

    with Cluster("Security OU"):
        security_ou = OrganizationsOrganizationalUnit("Security")

    with Cluster("Sandbox OU"):
        with Cluster("Sandbox SCPs", graph_attr={"style": "dashed", "color": "firebrick", "fontcolor": "firebrick"}):
            scp_region_sb = IAMPermissions("region-lockdown\nus-east-1 only")
        sandbox_ou = OrganizationsOrganizationalUnit("Sandbox")
        sandbox_acct = OrganizationsAccount("sandbox\naccount")

    with Cluster("Workloads OU"):
        with Cluster("Workloads SCPs", graph_attr={"style": "dashed", "color": "firebrick", "fontcolor": "firebrick"}):
            scp_region_wl = IAMPermissions("region-lockdown\nus-east-1 only")
            scp_s3_enc = IAMPermissions("require-s3\nencryption")
        workloads_ou = OrganizationsOrganizationalUnit("Workloads")

        with Cluster("Dev OU"):
            dev_ou = OrganizationsOrganizationalUnit("Dev")
            dev_acct = OrganizationsAccount("dev\naccount")

        with Cluster("Prod OU"):
            with Cluster("Prod SCPs", graph_attr={"style": "dashed", "color": "firebrick", "fontcolor": "firebrick"}):
                scp_ct = IAMPermissions("deny-cloudtrail\ntampering")
                scp_pub = IAMPermissions("deny-public-s3")
            prod_ou = OrganizationsOrganizationalUnit("Prod")
            prod_acct = OrganizationsAccount("prod\naccount")

    root >> Edge(color="gray") >> security_ou
    root >> Edge(color="gray") >> sandbox_ou
    root >> Edge(color="gray") >> workloads_ou

    sandbox_ou >> Edge(color="gray") >> sandbox_acct

    workloads_ou >> Edge(color="gray") >> dev_ou
    workloads_ou >> Edge(color="gray") >> prod_ou

    dev_ou >> Edge(color="gray") >> dev_acct
    prod_ou >> Edge(color="gray") >> prod_acct
