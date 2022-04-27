  // Question - 1
  console.log("Even Numbers from 1 to 100 in Descending Order :")
  for(var n=100;n>=1;n--){
      if (n%2==0){
          console.log(n)
      }
  }

  //Question - 2
  console.log("Multiplication Table :")
  var n = prompt("Enter the number you want to print Multiplication Table for :")
  var m = prompt("Enter the limit, till how much the table should be printed :")
  if (m==""){
      m=10
  }
  multiplication_table(n,m)
  
  function multiplication_table(n,m){
      n = Number(n)
      m = Number(m)
      for(let a=1;a<=m;a++){
          console.log(`${n} x ${a} = ${n*a}` )
      }
  }
