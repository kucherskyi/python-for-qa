"""
Having tuple ('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic',
'admin', '12345') with production database connection properties
(dialect, host, port, database name, user name, password), program should:

-create prod_config dictionary, where dict keys are connection properties
names and dict values are appropriate values from the input tuple;
-create staging_config dictionary with the same keys and values as prod_config;
-in staging_config change host to 'semantic.amazonaws-staging.com' and
password to 'root';
-for prod_config and staging_config print connection strings in the following
format {dialect}://{user name}:{password}@{host}:{post}/{database name}
"""

from copy import deepcopy


def conn_strings(env):
    prod_config = ('postgresql',
                   'semantic.amazonaws-prod.com',
                   5432,
                   'semantic',
                   'admin',
                   '12345')
    keys = ('dialect',
            'host',
            'port',
            'database name',
            'user name',
            'password')

    prod_config = dict(zip(keys, prod_config))
    staging_config = deepcopy(prod_config)
    staging_config['host'] = 'semantic.amazonaws-staging.com'
    staging_config['password'] = 'root'
    
    def make(envi):
        a = envi
        template = '{0}://{1}:{2}@{3}:{4}/{5}'.format(a['dialect'],
                                                      a['user name'],
                                                      a['password'],
                                                      a['host'],
                                                      a['port'],
                                                      a['database name'])
        return template
    
    if env == 'prod':
        return make(prod_config)
    elif env == 'staging':
        return make(staging_config)
    else:
        raise Exception ("Not valid environment")
        
print conn_strings('staging')

