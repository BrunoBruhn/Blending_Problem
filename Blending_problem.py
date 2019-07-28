	import pulp
	from gurobipy import *
	LP = pulp.LpProblem('LP',pulp.LpMinimize)  

	Cost=pulp.LpVariable("Cost",lowBound=0,cat=pulp.LpContinuous)

		
		#relative amounts of nutrients
	calcium_content=pulp.LpVariable("calcium_content",cat=pulp.LpContinuous,lowBound=0.008,upBound=0.012)
	protein_content=pulp.LpVariable("protein_content",cat=pulp.LpContinuous,lowBound=0.22)
	fiber_content=pulp.LpVariable("fiber_content",cat=pulp.LpContinuous,upBound=0.05)

	#ingredient units
	n_Limestone=pulp.LpVariable("n_Limestone",cat=pulp.LpContinuous,lowBound=0)
	n_Corn=pulp.LpVariable("n_Corn",cat=pulp.LpContinuous,lowBound=0)
	n_Soy=pulp.LpVariable("n_Soy",cat=pulp.LpContinuous,lowBound=0)
		#obj
	LP += n_Limestone*10 +n_Corn*30.5 +n_Soy*90

	LP += calcium_content	== (n_Limestone*0.38 	+n_Corn*0.001	+n_Soy*0.002)		#kg calcium
	LP += protein_content	== (n_Limestone*0 		+n_Corn*0.09	+n_Soy*0.5 	)		#kg protein
	LP += fiber_content		== (n_Limestone*0		+n_Corn*0.02	+n_Soy*0.08 )		#kg calcium
	LP += n_Limestone + n_Corn + n_Soy  			== 1 


	status = LP.solve(pulp.solvers.GUROBI(mip=True, msg=True, timeLimit=None,epgap=None))
	print( 'LP status: ' + pulp.LpStatus[status] + '')

	print(str(n_Limestone.value())+"kg Lime, "+str(n_Corn.value())+"kg Corn, "+str(n_Soy.value())+"kg Soy")




