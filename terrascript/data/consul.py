# terrascript/data/consul.py
import terrascript


class consul_agent_self(terrascript.Data):
    pass


class consul_agent_config(terrascript.Data):
    pass


class consul_autopilot_health(terrascript.Data):
    pass


class consul_nodes(terrascript.Data):
    pass


class consul_service(terrascript.Data):
    pass


class consul_service_health(terrascript.Data):
    pass


class consul_services(terrascript.Data):
    pass


class consul_keys(terrascript.Data):
    pass


class consul_key_prefix(terrascript.Data):
    pass


class consul_acl_auth_method(terrascript.Data):
    pass


class consul_acl_policy(terrascript.Data):
    pass


class consul_acl_role(terrascript.Data):
    pass


class consul_acl_token(terrascript.Data):
    pass


class consul_acl_token_secret_id(terrascript.Data):
    pass


class consul_network_segments(terrascript.Data):
    pass


class consul_network_area_members(terrascript.Data):
    pass


class consul_catalog_nodes(terrascript.Data):
    pass


class consul_catalog_service(terrascript.Data):
    pass


class consul_catalog_services(terrascript.Data):
    pass


__all__ = [
    "consul_agent_self",
    "consul_agent_config",
    "consul_autopilot_health",
    "consul_nodes",
    "consul_service",
    "consul_service_health",
    "consul_services",
    "consul_keys",
    "consul_key_prefix",
    "consul_acl_auth_method",
    "consul_acl_policy",
    "consul_acl_role",
    "consul_acl_token",
    "consul_acl_token_secret_id",
    "consul_network_segments",
    "consul_network_area_members",
    "consul_catalog_nodes",
    "consul_catalog_service",
    "consul_catalog_services",
]
