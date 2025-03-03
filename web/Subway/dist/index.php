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

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['vegetables']) || isset($_POST['sauces'])) {
        $encodedOrder = handleFormSubmit($_POST);
        echo "<p>Your encoded order: $encodedOrder</p>";
    } elseif (isset($_POST['encoded_order'])) {
        displayOrder($_POST['encoded_order']);
    }
}

function handleFormSubmit($formData) {
    $order = new Order($formData['vegetables'] ?? [], $formData['sauces'] ?? []);
    $serialized = serialize($order);
    return base64_encode($serialized);
}

function displayOrder($encodedOrder) {
    $decoded = base64_decode($encodedOrder);
    $order = unserialize($decoded);

    $vegetables = !empty($order->vegetables) ? implode(', ', $order->vegetables) : 'no vegetables';
    $sauces = !empty($order->sauces) ? implode(', ', $order->sauces) : 'no sauces';

    echo "<p>Your order is: Chicken Teriyaki 6 inch with $vegetables and $sauces.</p>";
    
    if ($order->admin) {
        header("Location: https://www.google.com"); # on second thought, i don't want anyone viewing my flag...
        echo "<p>The flag is: IRS{sample_flag}</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subway</title>
</head>
<body>
    <h1>Subway</h1>
    <p>Order: Chicken Teriyaki 6 inch</p>
    
    <form method="POST" action="">
        <fieldset>
            <legend>Add Vegetables:</legend>
            <label><input type="checkbox" name="vegetables[]" value="Lettuce"> Lettuce</label><br>
            <label><input type="checkbox" name="vegetables[]" value="Tomatoes"> Tomatoes</label><br>
            <label><input type="checkbox" name="vegetables[]" value="Onions"> Onions</label><br>
            <label><input type="checkbox" name="vegetables[]" value="Cucumbers"> Cucumbers</label><br>
            <label><input type="checkbox" name="vegetables[]" value="Olives"> Olives</label><br>
        </fieldset>

        <fieldset>
            <legend>Add Sauces:</legend>
            <label><input type="checkbox" name="sauces[]" value="Mayonnaise"> Mayonnaise</label><br>
            <label><input type="checkbox" name="sauces[]" value="Mustard"> Mustard</label><br>
            <label><input type="checkbox" name="sauces[]" value="Sweet Onion"> Sweet Onion</label><br>
            <label><input type="checkbox" name="sauces[]" value="Chipotle Southwest"> Chipotle Southwest</label><br>
            <label><input type="checkbox" name="sauces[]" value="BBQ Sauce"> BBQ Sauce</label><br>
        </fieldset>

        <button type="submit">Submit</button>
    </form>

    <h2>Enter Your Order</h2>
    <form method="POST" action="">
        <label for="encoded_order">Your order:</label><br>
        <textarea id="encoded_order" name="encoded_order" rows="4" cols="50"></textarea><br>
        <button type="submit">Submit order!</button>
    </form>
</body>
</html>
