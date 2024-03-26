Feature: Management of Deposits and Items

  # Scenarios related to login
  Scenario: Successful Login
    Given that the user has valid credentials
    When the user accesses the login page and enters their credentials
    Then the login is successfully performed
	
  Scenario: Login with Invalid Credential
    Given that the user has only one of the valid credentials
    When the user enters one valid and one invalid credential
    Then the login fails, and a message informs that there are invalid credentials
	
  Scenario: Password Recovery
    Given that the user has lost their password but has a valid email
    When the user submits the "forgot my password" field
    Then they are redirected to a password recovery page and receive an email with a link to reset the password

  # Scenarios related to Deposits
  Scenario: First Deposit Registration
    Given that no deposits are registered
    When the user accesses the deposit registration page
    Then the only available option is "New Deposit"
    
  Scenario: Filling in Registration Fields
    Given that the user is on the deposit registration page
    When the user fills in all fields with valid data
    Then the deposit is successfully created
    
  Scenario: Optional Fields in Registration
    Given that the user is on the deposit registration page
    When the user fills in only the optional fields
    Then the deposit should not be created
    
  Scenario: View Deposit
    Given that there are registered deposits
    When the user views the details of a specific deposit
    Then all fields filled in during registration are displayed
    
  Scenario: Deposit Editing
    Given that there are registered deposits
    When the user edits the details of a deposit
    Then the changes are successfully reflected
    
  Scenario: Delete Deposit
    Given that there are registered deposits
    When the user deletes a deposit
    Then the deposit is removed from the list of deposits
	
  Scenario: Deleting a Deposit Associated with an Item
    Given that a deposit is associated with an item
    When the user deletes this item
    Then the item is not removed from the list

  # Scenarios related to Items
  Scenario: New Item Registration
    Given that no item is registered
    When the user accesses the item registration page
    Then the only available option is "New Item"
    
  Scenario: Filling in Registration Fields
    Given that the user is on the item registration page
    When the user fills in all fields with valid data
    Then the item is created successfully
    
  Scenario: Optional Fields in Registration
    Given that the user is on the item registration page
    When the user fills in only the optional fields
    Then the item is not created
    
  Scenario: View Item
    Given that there are registered items
    When the user views the details of a specific item
    Then all fields filled in during registration are displayed
    
  Scenario: Item Editing
    Given that there are registered items
    When the user edits the details of an item
    Then the changes are successfully reflected
    
  Scenario: Delete Item
    Given that there are registered items
    When the user destroys an item
    Then the item is removed from the list of items
	
  Scenario: Deleting an Item Associated with a Deposit
    Given that an item is associated with a deposit
    When the user destroys this item
    Then the item is not removed from the list

  # Scenarios related to Inventory
  Scenario: Create New Inventory
    Given that there are registered items and deposits
    When the user creates a new inventory and associates an item and a deposit
    Then the inventory is created successfully
	
  Scenario: Create New Inventory with Item and Deposit Previously Associated with Another Inventory
    Given that there is an inventory using a specific item and deposit
    When the user tries to create a new inventory and associate this item and/or deposit
    Then the inventory is not created, and a message informs that this item and/or deposit is already assigned to another inventory

  Scenario: Create New Inventory with Deposit and without Item
    Given that there are registered items and deposits
    When the user tries to associate a new inventory with an item and leaves the deposit field blank
    Then the inventory should not be created, and a message informs that the deposit cannot be left blank
	
  Scenario: Create New Inventory with Item and without Deposit
    Given that there are registered items and deposits
    When the user tries to associate a new inventory with a deposit and leaves the item field blank
    Then the inventory should not be created, and a message informs that the item cannot be left blank

  Scenario: View Inventory
    Given that there are registered inventories
    When the user views the details of a specific inventory
    Then all fields filled in during registration are displayed

  Scenario: Edit Inventory
    Given that there are registered inventories
    When the user edits the details of an inventory with an item and deposit free of previous association
    Then the changes are successfully reflected
  
  Scenario: Delete Inventory
    Given that there are registered inventories
    When the user deletes an inventory
    Then the inventory is removed from the list of inventories
