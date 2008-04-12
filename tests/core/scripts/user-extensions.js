	// The "inDocument" is a the document you are searching.
	PageBot.prototype.locateElementByValueRepeated = function(text, inDocument) {
	    // Create the text to search for
	    var expectedValue = text + text;
	
	    // Loop through all elements, looking for ones that have 
	    // a value === our expected value
	    var allElements = inDocument.getElementsByTagName("*");
	    for (var i = 0; i < allElements.length; i++) {
	        var testElement = allElements[i];
	        if (testElement.value && testElement.value === expectedValue) {
	            return testElement;
	        }
	    }
	    return null;
	};

	Selenium.prototype.assertValueRepeated = function(locator, text) {
	    // All locator-strategies are automatically handled by "findElement"
	    var element = this.page().findElement(locator);
	
	    // Create the text to verify
	    var expectedValue = text + text;
	
	    // Get the actual element value
	    var actualValue = element.value;
	
	    // Make sure the actual value matches the expected
	    Assert.matches(expectedValue, actualValue);
	};

	Selenium.prototype.getTextLength = function(locator, text) {
		return this.getText(locator).length;
	};

	Selenium.prototype.assertBalanceEqual = function(oldBalance, currentBalance) 
	{
		oldBalance = oldBalance.split('$')[1];
		currentBalance = currentBalance.split('$')[1];
		Assert.matches(expectedValue, actualValue);
	}

