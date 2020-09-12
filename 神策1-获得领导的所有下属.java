员工领导之间的关系

员工     领导
Alice    Bob
Steve    Isaac
Oscar    Bob
Isaac    Walter

private HashMap<String, List<String>> leader2Employee = new HashMap<>(); // 储存{领导: [员工1, 员工2......]}

void add(String employee, String leader) {
    List<String> nowList = leader2Employee.getOrDefault(leader, new ArrayList<String>());
    nowList.add(employee);
    leader2Employee.put(leader, nowList);
}

/**
 * 返回 leader 一共有多少下属，包括间接下属
 */
int fun1(String leader) {
    int count = 0;
    Stack<String> dfs = new Stack<>();
    dfs.push(leader);
    while(dfs.size() != 0) {
        String nowName = dfs.pop();
        count++;
        List<String> employees = leader2Employee.get(nowName);
        for(String name : employee)
            dfs.push(name);
    }
    return count - 1;//不包括自己
}