# RBAC_diff

```
curl -k -XGET -H 'Authorization: Bearer XXXXX' "https://kazu-01.sysdiglabs.com/api/admin/security/roles/documentation?product=SDS" | jq > RBAC_5.1.9
```

```
curl -k -XGET -H 'Authorization: Bearer XXXXX' "https://kazu-02.sysdiglabs.com/api/admin/security/roles/documentation?product=SDS" | jq > RBAC_6.0.3
```

- Test env
https://sysdig.atlassian.net/wiki/spaces/~7120200f8d79d7ab3a49fdb29b5f5e4df9cb7a/pages/3031498753/On-prem+v5.1.9+and+v6.3+RBAC+diff
