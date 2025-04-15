import csv
import random
import copy

#Project Scheduling Evolutionary Algorithm 
class SchedulingEvolutionaryAlgorithm():
    #File location for the CSV files
    workerCSVfilepath = ""
    jobsCSVfilepath = ""
    taskDurationCSVfilepath = ""
    #Saving the data from CSV files into dictionaries
    workers_dict = {}
    jobs_dict = {}
    taskDuration_dict = {}
    jobs_graph = {}
    no_of_jobs = 0
    #Algorithm parameters
    population = []
    populationSize = 0
    populationSizeMax = 0
    crossoverChance = 0
    mutationChance = 0
    generation = -1
    oldGeneration = -1
    #Best result
    bestChromosome = None
    #Initialize function
    def __init__(self,workerCSVfilepath,jobsCSVfilepath,taskDurationCSVfilepath):
        self.workerCSVfilepath = workerCSVfilepath
        self.jobsCSVfilepath = jobsCSVfilepath
        self.taskDurationCSVfilepath = taskDurationCSVfilepath
        #Load the CSV files into the dictionaries
        self.workers_dict = self.CSV_To_Dict(self.workerCSVfilepath)
        self.jobs_dict  = self.CSV_To_Dict(self.jobsCSVfilepath)
        self.taskDuration_dict = self.CSV_To_Dict(self.taskDurationCSVfilepath)
        #Create new worker_dict
        new_dict = {}
        for i in range(len(self.workers_dict["ID"])):
            new_dict[self.workers_dict["ID"][i]]={"Name":self.workers_dict["Name"][i],"Role":self.workers_dict["Role"][i]}
        self.workers_dict = new_dict
        #Create new jobs_dict
        new_dict = {}
        for i in range(len(self.jobs_dict["ID"])):
            if self.jobs_dict["Predecessor"][i] == '':
                new_dict[self.jobs_dict["ID"][i]]={"Name":self.jobs_dict["Name"][i],"Predecessor":[]}
            else:
                new_dict[self.jobs_dict["ID"][i]]={"Name":self.jobs_dict["Name"][i],"Predecessor":self.jobs_dict["Predecessor"][i].split(",")}
        self.jobs_dict = new_dict
        #Make a new taskDuration_dict for faster calculations
        new_dict= {}
        for key,value in self.jobs_dict.items():
            new_dict[key]=[]

        for i in range(len(self.taskDuration_dict["JobID"])):
            new_dict[self.taskDuration_dict["JobID"][i]].append({"WorkersID":self.taskDuration_dict["WorkersID"][i].split(","),"EstimatedTime":float(self.taskDuration_dict["EstimatedTime"][i])})
        self.taskDuration_dict = new_dict
        #Making sure all the predecessors listed in jobs_dict are unique
        for key,value in self.jobs_dict.items():
            _unique_array = []
            [_unique_array.append(item) for item in value["Predecessor"] if item not in _unique_array]
            value["Predecessor"] = _unique_array
        #Making sure all the workersID listed in taskDuration_dict are unique
        for key,value in self.taskDuration_dict.items():
            for item in value:
                _unique_array = []
                [_unique_array.append(item) for item in item["WorkersID"] if item not in _unique_array]
                item["WorkersID"] = _unique_array
        #Generate the jobs dependencies graph
        self.jobs_graph = self.generate_jobs_graph()
        #Save number of jobs for faster computation
        self.no_of_jobs = len(self.jobs_dict)
    #Set Algorithm Parameters
    def setParameters(self,popSize, crossoverChance, mutationChance):
        self.populationSizeMax = popSize
        self.crossoverChance = crossoverChance
        self.mutationChance = mutationChance 
    #Initialize the first population
    def initialize_population(self):
        self.generation = 0
        self.population = []
        for _ in range(self.populationSizeMax):
            chromosome = self.create_chromosome()
            self.population.append(chromosome)
        self.populationSize = self.populationSizeMax
        self.bestChromosome = copy.deepcopy(self.population[0])
        return  self.population
    #Evolve Function
    def evolve(self):
        new_population = []
        #Fill population with new members from the old members
        self.generation +=1
        self.population.append(self.bestChromosome)
        while len(new_population) < self.populationSizeMax:
            parent0, parent1 = self.select_parents()
            if random.random() < self.crossoverChance:
                offspring0, offspring1 = self.crossover(parent0,parent1)
            else:
                offspring0, offspring1 = copy.deepcopy(parent0), copy.deepcopy(parent1)
            if random.random() < self.mutationChance:
                offspring0 = self.mutation(offspring0)
            if random.random() < self.mutationChance:
                offspring1 = self.mutation(offspring1)
            new_population.append(offspring0)
            new_population.append(offspring1)
        self.population = new_population
        #self.population.extend(new_population)
        #self.population = sorted(self.population, key=lambda chromosome: chromosome["fitness"],reverse=True)
        #self.population=self.population[:self.populationSizeMax]
        self.populationSize = len(self.population)
        self.bestChromosome = copy.deepcopy(self.ranked_population[0])
        #self.bestChromosome = max(self.population, key=lambda x: x['fitness'])
    #Select parents
    def select_parents(self):
        return self.select_parents_rank_based()
    #Stochastic Sampling
    def select_parents_stochastic_universal_sampling(self):
        # Select parents
        if self.generation != self.oldGeneration:
            self.oldGeneration = int(self.generation)
            #Calculate total fitness, selection probabilities and cumulative probabilities for the stochastic universal sampling
            # Calculate total fitness
            self.total_fitness_stochastic = sum(chromosome["fitness"] for chromosome in self.population)
            # Calculate selection probability for each individual
            self.selection_probabilities_stochastic = [chromosome["fitness"] / self.total_fitness_stochastic for chromosome in self.population]
            # Create a list of cumulative probabilities
            self.cumulative_probabilities_stochastic = [sum(self.selection_probabilities_stochastic[:i+1]) for i in range(self.populationSize)]
            
        parents = []
        startPoint = random.uniform(0, self.total_fitness_stochastic / 2)
        pointer = startPoint
        current_index = 0
        for _ in range(2):
            while self.cumulative_probabilities_stochastic[current_index] < pointer:
                current_index += 1
            parents.append(self.population[current_index])
            pointer += self.total_fitness_stochastic / 2
        return parents[0], parents[1]
    #Rank Based selection
    def select_parents_rank_based(self):
        if self.generation != self.oldGeneration:
            self.oldGeneration = int(self.generation)
            # Rank individuals based on their fitness
            self.ranked_population = sorted(self.population, key=lambda chromosome: chromosome["fitness"],reverse=True)
            # Assign selection probabilities based on rank
            self.selection_probabilities = [(len(self.ranked_population) - i) / len(self.ranked_population) for i in range(len(self.ranked_population))]

        # Select parents probabilistically
        parents = random.choices(population=self.ranked_population, weights=self.selection_probabilities,k=2)

        return parents[0], parents[1]
    #Generate a graph that shows for each job who is the parent / children + include start node
    def generate_jobs_graph(self):
        graph = {"Start":{"parents":[],"children":[]}}
        #generate parents list for each node
        for key,value in self.jobs_dict.items():
            row={"ID":key,"Name":value["Name"],"Predecessor":value["Predecessor"]}
            graph[row["ID"]]={"parents":row["Predecessor"],"children":[]}
            if graph[row["ID"]]["parents"]==[]:
                graph[row["ID"]]["parents"]=["Start"]
        #generate children list for each node
        for key, value in graph.items():
            for parent in value["parents"]:
                graph[parent]["children"].append(key)
        return graph
    
    #Load CSV files into Dictionary
    def CSV_To_Dict(self,path):
        data = {}
        with open(path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for key, value in row.items():
                    if key in data:
                        data[key].append(str(value))
                    else:
                        data[key] = [str(value)]
        return data
    #Create a chromosome for initial population
    #   This creates a new chromosome containing a job/worker assignment for each job
    #   And makes a job priority so fitness can be computed
    #   The job/worker assignment are from time_dict, and jobs_dict to check which jobs exist
    def create_chromosome(self):
        #Create genes_dict with the genes that compose the chromosome
        gene_dict = {}
        #For each job in job_dict
        for key,value in self.jobs_dict.items():
            randomInt = random.randint(0,len(self.taskDuration_dict[key])-1)
            #Pick random job/worker assignment from TaskDurationDict
            gene = {"WorkersID":self.taskDuration_dict[key][randomInt]["WorkersID"],"EstimatedTime":self.taskDuration_dict[key][randomInt]["EstimatedTime"]}
            #Add gene
            gene_dict[key]=gene
        #Calculate the fitness of the chromosome
        priority = self.generate_priority()
        fitness = self.fitness(gene_dict,priority)
        return {"genes":gene_dict, "priority":priority, "fitness":fitness}
    #Generate a random job priority for a new schedule
    def generate_priority(self):
        #The list of jobs that are fulfill the requirement to be worker right away
        job_choices = [i for i in self.jobs_graph["Start"]["children"]]
        #Initialize the priority list
        priority = []
        #List of jobs that are already put in the priority list
        jobs_listed = {}
        #Set all jobs as not being used in the priority list yet
        for key,_ in self.jobs_graph.items():
            jobs_listed[key]=False
        #Except for the Start Node that will be used now to traverse the graph
        jobs_listed["Start"]=True
        #Repeat until the job graph was fully traversed or can not be traversed anymore
        while len(job_choices)>0:
            #Pick a random job from the nodes that can be put in the priority list
            randomInt = random.randint(0, len(job_choices)-1)
            picked_job = job_choices.pop(randomInt)
            #Put the chosen job in the priority list
            jobs_listed[picked_job] = True
            priority.append(picked_job)
            #Check which child of the picked job can be considered next in the priority list
            #A child is acceptable if all its parent nodes are already in the priority list
            for picked_job_child in self.jobs_graph[picked_job]["children"]:
                acceptable = True
                for picked_job_child_parent in self.jobs_graph[picked_job_child]["parents"]:
                    if jobs_listed[picked_job_child_parent] == False:
                        acceptable = False
                        break
                if acceptable:
                    job_choices.append(picked_job_child)
        #Priority list is finished
        return priority
    
    #Repair function for the priority
    #   Sometimes after mutations / crossover the priority part of the chromosome will become invalid, this fixes it
    def repair_priority(self, _old_priority):
        old_priority = copy.deepcopy(_old_priority)
        #Pick a random job from the nodes that can be put in the priority list
        job_choices = [i for i in self.jobs_graph["Start"]["children"]]
        #Initialize the new priority list
        priority = []
        #List of jobs that are already put in the priority list
        jobs_listed = {}
        #Set all jobs as not being used in the priority list yet
        for key,_ in self.jobs_graph.items():
            jobs_listed[key]=False
        #Except for the Start Node that will be used now to traverse the graph
        jobs_listed["Start"]=True
        #Repeat until the job graph was fully traversed or can not be traversed anymore
        while len(job_choices)>0:
            #Same thing like in the generation of the priority list, but instead of picking a random job that can be traversed, pick the first job in the priority list that can be traversed.
            #If a job in the priority list can not be traversed yet, put it to the end of the priority list
            while not(old_priority[0] in job_choices):
                old_priority.append(old_priority.pop(0))
            #Get the first job in the old priority that is valid to be used in the new priority
            picked_job = old_priority.pop(0)
            job_choices.remove(picked_job)
            #Put the chosen job in the priority list
            jobs_listed[picked_job] = True
            priority.append(picked_job)
            #Check which child of the picked job can be considered next in the priority list
            #A child is acceptable if all its parent nodes are already in the priority list
            for picked_job_child in self.jobs_graph[picked_job]["children"]:
                acceptable = True
                for picked_job_child_parent in self.jobs_graph[picked_job_child]["parents"]:
                    if jobs_listed[picked_job_child_parent] == False:
                        acceptable = False
                        break
                if acceptable:
                    job_choices.append(picked_job_child)
        return priority
    
    #Fitness function
    #This simulates the schedule
    def fitness(self, _genes, _priority):
        genes = copy.deepcopy(_genes)
        priority = copy.deepcopy(_priority)
        #A list of the time when each worker task
        worker_finish_time = {}
        #A list of times when each job is finished
        job_finish_time = {}
        #Start node is 0
        job_finish_time["Start"] = 0
        #Set job finish time to 0
        for key,_ in genes.items():
            job_finish_time[key] = 0
        #Set worker finish time to 0
        for key,value in self.workers_dict.items():
            worker_finish_time[key] = 0
        #Find the maximum finish time for each job and worker
        for i in priority:
            #Calculate earliest task start
            maximum=0
            #calculate when latest parent task ends
            maximum = max(maximum,max([job_finish_time[j] for j in self.jobs_graph[i]["parents"]]))
            #Calculate when the latest worker can start
            maximum= max(maximum,max( [worker_finish_time[j] for j in genes[i]["WorkersID"]]))
            #Then add the estimated time to it
            maximum = maximum + float(genes[i]["EstimatedTime"])
            #Now set job_i's finish time
            job_finish_time[i] = maximum
            #Set all workers that did the job_i to be busy till the job is done
            for j in genes[i]["WorkersID"]:
                worker_finish_time[j] = maximum
        return -max([i for _,i in job_finish_time.items()])
    
    #Mutation function
    def mutation(self, _chromosome):
        chromosome = copy.deepcopy(_chromosome)
        genes = chromosome["genes"]
        priority = chromosome["priority"]
        #Pick random gene to mutate
        random_job_id = list(genes.keys())[random.randint(0,self.no_of_jobs-1)]
        #Find a new gene to mutate into from taskDuration_dict
        random_gene_id = random.randint(0,len(self.taskDuration_dict[random_job_id])-1)
        new_gene = {"WorkersID":self.taskDuration_dict[random_job_id][random_gene_id]["WorkersID"],"EstimatedTime":self.taskDuration_dict[random_job_id][random_gene_id]["EstimatedTime"]}
        #Assign the same rows as in last chromosome and the mutated gene
        genes[random_job_id] = new_gene
        #Push the randomly chosen gene's order to the end
        priority.append(priority.pop(priority.index(random_job_id)))
        priority = self.repair_priority(priority)
        #Calculate new fitness
        fitness = self.fitness(genes,priority)
        return {"genes":genes, "priority":priority, "fitness":fitness}

    #Crossover function
    def crossover(self, _parent0, _parent1):
        parent0 = copy.deepcopy(_parent0)
        parent1 = copy.deepcopy(_parent1)
        genes0 = parent0["genes"]
        priority0 = parent0["priority"]
        genes1 = parent1["genes"]
        priority1 = parent1["priority"]
        #Choose randomly what genes are passed
        split_index = random.randint(0,self.no_of_jobs-1)
        swapped = random.choice([(True,True),(True,False),(False,True),(False,False)])
        #Initialize childrens
        childGene0 = {}
        childGene1 = {}
        childPriority0 = []
        childPriority1 = []
        #Creating children genes from parents
        keys = list(genes0.keys())
        for i, key in enumerate(keys):
            if i < split_index:
                childGene0[key] = genes0[key]
                childGene1[key] = genes1[key]
            else:
                childGene0[key] = genes1[key]
                childGene1[key] = genes0[key]
        #Creating children priority lists from parents
        childPriority0 = priority0[:split_index]
        for i in priority1:
            if i not in childPriority0:
                childPriority0.append(i)
        childPriority1 = priority1[:split_index]
        for i in priority0:
            if i not in childPriority1:
                childPriority1.append(i)
        #Making sure the children priority lists are valid
        childPriority0 = self.repair_priority(childPriority0)
        childPriority1 = self.repair_priority(childPriority1)
        #Swap children priorities for more randomness
        if not swapped:
            return {"genes":childGene0, "priority":childPriority0, "fitness":self.fitness(childGene0,childPriority0)},{"genes":childGene1, "priority":childPriority1, "fitness":self.fitness(childGene1,childPriority1)}
        return {"genes":childGene0, "priority":childPriority1, "fitness":self.fitness(childGene0,childPriority1)},{"genes":childGene1, "priority":childPriority0, "fitness":self.fitness(childGene1,childPriority0)}