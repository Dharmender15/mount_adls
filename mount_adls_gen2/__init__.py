class Configs:
  def __init__(self, client_id, client_secret, tenant_id):
    """
      Configs(...)
        configs = Configs()
        
        Initializes client_id, client_secret and tenant_id.
        Required arguments:
        client_id:      client_id of application
        client_secret:  client_secret of application
        tenant_id:      tenant_id
    """
    self.client_id = client_id
    self.client_secret = client_secret
    self.tenant_id = tenant_id
  
  def get_configs(self):
    """
      get_configs(...)
        configs = Configs()
        extra_configs = configs.get_configs()
        
        Returns the extra configs required to mount ADLS.
    """
    return {
      "fs.azure.account.auth.type": "OAuth",
      "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
      "fs.azure.account.oauth2.client.id": self.client_id,
      "fs.azure.account.oauth2.client.secret": self.client_secret,
      "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"
    }
