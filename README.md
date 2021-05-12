# share_price_tracker

#### For the long term investors, It is not necessary to keep track of the prices of shares they bought every day. They invest lumsome amount on some shares and wait for targeted returns say after 30% or 50% of profit or other way could be to save losses below a certain amount. so it is important that once the target is hit then the investor should be notified. so for that, we can write a peice of code which will do our work and notify us via a email.

#### Using the BSEDATA library, we get all the information about the companies listed at Bombay Stock Exchange (BSE). each company has a unique code and we can get all the information of a particular company by querying using library functions. The "companies.txt" file contains the codes for all the companies listed at BSE. In the code we are tracking prices of some stocks mentioned in code comments.

#### Using SMTP library to send mail to the user when the target is hit.

#### As this is a real-time project, the code script needs to be running all the time. for that it requires a virtual machine access, where the python script can run all the time on server. This is a crucial resource requirement for the execution of the project.  
