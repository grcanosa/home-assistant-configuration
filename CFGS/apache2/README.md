# Installation Instructions

```bash 
sudo apt-get install apache2 -y
```

## Configuration

Copy the *.conf files to /etc/apache2/sites-available.
Enable the sites with:

```
sudo a2ensite grcanosa*.conf
```

The enable the modules:

```
sudo a2enmod rewrite
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_wstunnel
```

To check the configuration:

``` 
apachectl configtest
```

To check the logs:

```
tail /var/log/apache2/error.log
```