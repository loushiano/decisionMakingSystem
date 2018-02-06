# decisionMakingSystem
a decision making system to control simulated self driving cars in both truevision.ai and airsim
first you need to download the following python packages:


AirSim:
If you want to work with AirSim, you have to download an environmnet from their main repository here.
After you download the simulation environment, all you need to do is to run our program.
if the connection fails between our program and the simulation environment, follow the steps mentioned here.
We are working with the cinty Environment in their realease version.

TrueVision:




OtherEnvironments:
If you want to work on or test our program with another simulation environment, you have to create another AdapterEnvironment concrete class that inherits from our AdapterEnvironment, and make the right connections, or write a compatible interface between the environment you chose and our program. Make sure you only implement the methods that we have defined in the abstract class AdapterEnvironment.

