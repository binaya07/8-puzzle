import sys
import game
import stack
import queue

goal_list = [0,1,2,3,4,5,6,7,8]
 
def dls_search(begin_state,zero_pos):
    puzzle_state = game.Game(begin_state,zero_pos)
    stck = stack.Stack()
    
    for depth_limit in range(1,5):
        i=0
        explored = set()  #to store already explored puzzle lists
        stck.push(puzzle_state)
        print("\n\tdepth limit : ",depth_limit)
        state = puzzle_state
        
        while (state.cost < depth_limit) or (not stck.isEmpty()):
            state = stck.pop() 
            print("iteration : ",i)    
            print(state.list)
            explored.add(tuple(state.list))
              
            if(state.list == goal_list):
                print("\n=========GOAL REACHED=========")
                write_to_file(state,i,"depth limit search")
                return 1
            
            children = []
            children.extend(state.expand())
            children.reverse()    
            
            if (state.cost < depth_limit):
                for states in children:
                    if tuple(states.list) not in (explored.union(stck.state)):
                        stck.push(states)
                        
            i = i+1
        
        explored.clear()
        stck.clear_stack()            
            
    print("\n======FAILED======")    
    
    
def dfs_search(begin_state,zero_pos):
    puzzle_state = game.Game(begin_state,zero_pos)
    stck = stack.Stack()
    
    depth_limit = 25
    i=0
    explored = set()  #to store already explored puzzle lists
    stck.push(puzzle_state)
    state = puzzle_state
    
    while (state.cost < depth_limit) or (not stck.isEmpty()):
        state = stck.pop() 
        print("iteration : ",i)    
        print(state.list)
        explored.add(tuple(state.list))
              
        if(state.list == goal_list):
            print("\n=========GOAL REACHED=========")
            write_to_file(state,i,"depth first search")
            return 1
        
        children = []
        children.extend(state.expand())
        children.reverse()    
        
        if (state.cost < depth_limit):
            for states in children:
                if tuple(states.list) not in (explored.union(stck.state)):
                    stck.push(states)
                    
        i = i+1
            
    print("\n======FAILED======")
    
    
def bfs_search(begin_state,zero_pos):
    puzzle_state = game.Game(begin_state,zero_pos)
    
    q = queue.Queue()
    q.enqueue(puzzle_state)
    explored = set()  #to store already explored puzzle lists
    i=0
    
    while not q.isEmpty():
        state = q.dequeue()
        print("iteration : ",i)
        print(state.list)
        explored.add(tuple(state.list))
        
        if(state.list == goal_list):
            print("\n=========GOAL REACHED=========")
            write_to_file(state,i,"breadth first search")
            return 1
        
        children = state.expand()
        for states in children:
            if tuple(states.list) not in (explored.union(q.state)):
                q.enqueue(states)  
        i = i+1

    print("\n======FAILED======")  
    
def write_to_file(state,i,string):
     cost = "path_cost : " + str(state.cost)
     nodes = "nodes_expanded :" + str(i)
     action_list = []
     for i in range(state.cost):
         action_list.append(state.action)
         state = state.parent
     action_list.reverse()
    
     Text = [cost+"\n",nodes+"\n"]
     with open("search_details.txt","w") as file1:
         
         file1.write("Search technique = " + string +"\n")
         for line in Text:
             file1.write(line)
         file1.write("action = [ ")
         for each in action_list:
             file1.write(each+", ")
         file1.write( "]")
         
    
    
def main():
      
    sm = sys.argv[1]
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state)) #converting from char to int 
     
    if(not len(begin_state)==9):
        print("Error: enter 9 numbers in arg2")
        sys.exit()
   
    for i,state in enumerate(begin_state):
        if state == 0:
            zero_pos = i 
    
         
    if sm == "bfs" or sm == "BFS":
        bfs_search(begin_state,zero_pos)

    elif sm == "dfs" or sm == "DFS":
        dfs_search(begin_state,zero_pos)
        
    elif sm=="dls" or sm=="DLS":
        dls_search(begin_state,zero_pos)
        
    elif sm == "ast" or sm == "AST":
        print("ast")
        #A_star_search(hard_state)

    else:
        print("bfs or dfs or ast as method type")
   
    
if __name__ == '__main__':

    main()
