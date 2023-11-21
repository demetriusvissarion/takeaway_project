Here is a project to test your golden square skills overall:

> As a customer  
> So that I can check if I want to order something  
> I would like to see a list of dishes with prices.
> 
> As a customer  
> So that I can order the meal I want  
> I would like to be able to select some number of several available dishes.   
=> both numbered dishes and qty, so two inputs (Eoin)
> 
> As a customer  
> So that I can verify that my order is correct  
> I would like to see an itemised receipt with a grand total. 

Use the `twilio-python` package to implement this next one. You will need to use mocks too.

> As a customer  
> So that I am reassured that my order will be delivered on time  
> I would like to receive a text such as "Thank you! Your order was placed and
> will be delivered before 18:52" after I have ordered." 
=> use the API manually to see if it works and after just mock it for all other tests (Eoin)

Fair warning: if you push your Twilio API Key to a public GitHub repository,
anyone will be able to see and use it. What are the security implications of
that? How will you keep that information out of your repository? 
=> save API key to file and add file to .gitignore