import traceback
from pyspark.dbutils import DBUtils
from mount_adls_gen2.__init__ import Configs

class Mount:
  def __init__(self, spark):
    """
      Mount(...)
        mount = Mount(spark)
        
        Initializes dbutils using spark session.
        Required arguments:
        spark:  current SparkSession
    """
    self.dbutils = DBUtils(spark)

  def mount_with_access_key(self, container_name, storageacc_name, mount_point, access_key):
    """
      mount_with_access_key(...)
        mount = Mount(spark)
        mount.mount_with_access_key(...)
        
        Mounts the ADLS using access keys.
        Required arguments:
        container_name:   container name of storage account
        storageacc_name:  storage account name
        mount_point:      the mount point you want to give
        access_key:       access key of storage account
    """
    source = f"wasbs://{container_name}@{storageacc_name}.blob.core.windows.net/"
    try:
      self.dbutils.fs.mount(
        source = source,
        mount_point = mount_point,
        extra_configs = {f"fs.azure.account.key.{storageacc_name}.blob.core.windows.net": access_key})
      print(f"{source} mounted to {mount_point}.")
    except:
      traceback.print_exc()

  def mount_adls(self, configs, container_name, storageacc_name, mount_point):
    """
      mount_adls(...)
        mount = Mount(spark)
        mount.mount_adls(...)
        
        NOTE: Needs to have Storage Blob Data Contributor access for Azure AD application on the ADLS Gen2 storage account.

        Mounts the ADLS using client id, client secret and tenant id.
        Required arguments:
        configs:          Configs object
        container_name:   container name of storage account
        storageacc_name:  storage account name
        mount_point:      the mount point you want to give
    """

    extra_configs = configs.get_configs()
    source = f"abfss://{container_name}@{storageacc_name}.dfs.core.windows.net/"
    
    try:
      self.dbutils.fs.mount(
        source = source,
        mount_point = mount_point,
        extra_configs = extra_configs)
      print(f"{source} mounted to {mount_point}.")
    except:
      traceback.print_exc()

  def unmount(self, mount_point):
    """
      unmount(...)
        mount = Mount(spark)
        mount.unmount(...)
        
        Unounts the ADLS account.
        Required arguments:
        mount_point:  the mount point you want to give
    """
    try:
      self.dbutils.fs.unmount(mount_point)
    except:
      traceback.print_exc()