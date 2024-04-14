%sustreg: realiza el despeje para la matriz triangular superior aumentada
% Ab, que da solución al sistema Ax=b Donde A es de tamaño nxn y b de tamaño nx1

function x=sustreg(Ab,n)
    x=zeros(n,1);
    x(n)=Ab(n,n+1)/Ab(n,n);
    for i=n-1:-1:1
        sum=0;
        for p=i+1:n
            sum=sum+Ab(i,p)*x(p);
        end
        x(i)=(Ab(i,n+1)-sum)/Ab(i,i);
    end
    
end