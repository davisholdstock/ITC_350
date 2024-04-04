CREATE USER 'webuser'@'172.16.32.7' IDENTIFIED BY '<your-password>'

GRANT SELECT INSERT UPDATE DELETE ON cupboard_cooking.* TO '<insert_name>'@'172.16.32.7'