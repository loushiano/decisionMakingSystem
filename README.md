# decisionMakingSystem
a decision making system to control simulated self driving cars in both truevision.ai and airsim
first you need to download the following python packages:


AirSim:
If you want to work with AirSim, you have to download an environmnet from their main repository. To download 
the simulation environmnet you must go [here](https://github.com/Microsoft/AirSim/releases).
After you finish downloading the simulation environment, all you need to do is to run the environment then to run our program.
not that you must import the Python client package from the airsim source code.
We are currently working with the cinty Environment provided by AirSim in the realase version v.1.1.7.
If you want to use an environment built on the Unreal Version but that is not provided by AirSim, follow this [tutorial](https://www.youtube.com/watch?v=y09VbdQWvQY)

TrueVision:




OtherEnvironments:
If you want to work on or test our program with another simulation environment, you have to create another AdapterEnvironment concrete class that inherits from our AdapterEnvironment class, and make the right connections, or write a compatible interface between the environment you chose and our program. Make sure you only implement the methods that we have defined in the abstract class AdapterEnvironment.

