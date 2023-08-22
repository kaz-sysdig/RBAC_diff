# RBAC_diff

curl -k -XGET -H 'Authorization: Bearer XXXXX' "https://kazu-01.sysdiglabs.com/api/admin/security/roles/documentation?product=SDS" | jq > RBAC_5.1.9
curl -k -XGET -H 'Authorization: Bearer XXXXX' "https://kazu-02.sysdiglabs.com/api/admin/security/roles/documentation?product=SDS" | jq > RBAC_6.0.3
