# https://www.hackerrank.com/challenges/grading/problem

vector<int> gradingStudents(vector<int> grades) {
    
    int diff, add;
    
    for (int i = 0; i < grades.size(); i++)
    {
        if (grades[i] >= 38) 
        {
            diff = grades[i] % 5;
            add = 5 - diff;
            
            if (add < 3) 
            {
                grades[i] += add;
            }
        }
    }
    
    return grades;
}

