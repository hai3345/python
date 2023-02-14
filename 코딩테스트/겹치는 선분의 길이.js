function solution(lines) {

    
    let sets = []

    for(let i = 0; i<=lines.length-1; i++ ){
        
        sets[i] = new Set(lines[i])
        
        
        console.log(sets[i])
    }
    

    var answer = 0;
    
    return answer;
    
}


lines = [[2, 5], [3, 6], [5, 7]]

solution(lines)