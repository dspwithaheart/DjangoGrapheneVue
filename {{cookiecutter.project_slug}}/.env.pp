SECRET_KEY=lizpdph7g61h!vprq(oq1z311yky4#c(6^b(9z=x36171{{cookiecutter.project_slug}}ifto
ENV=DD
ALLOWED_HOSTS={{cookiecutter.project_slug}}.services.domain-name.com
TAG_VERSION=0.1.0
{{cookiecutter.project_slug.upper()}}_DB_HOST=oda01.domain-name.com
{{cookiecutter.project_slug.upper()}}_DB_PORT=1521
{{cookiecutter.project_slug.upper()}}_DB_SERVICE=srdd.domain-name.com
{{cookiecutter.project_slug.upper()}}_DB_USER=++++++
{{cookiecutter.project_slug.upper()}}_DB_PASSWORD=+++
{{cookiecutter.project_slug.upper()}}_DB_TEST_USER=++++++
{{cookiecutter.project_slug.upper()}}_DB_TEST_PASSWORD=++++++
PROXY_SUBDOMAIN={{cookiecutter.project_slug}}
PROXY_DOMAIN=services-test.domain-name.com
PROXY_NETWORK=reverse-proxy_service-discovery
# LDAP https://django-auth-ldap.readthedocs.io/en/latest/example.html
AUTH_LDAP_SERVER_URI=ldap://ldaplocal....
AUTH_LDAP_BIND_DN="CN=<LDAP_CN>,OU=<....>,DC=<....>"  # dn string for binding
LDAP_CN=++++++
LDAP_PW=++++++