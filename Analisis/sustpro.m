%sustpro: realiza el despeje para la matriz triangular inferior aumentada
% Ab, que da solución al sistema Ax=b Donde A es de tamaño nxn y b de tamaño nx1

function x=sustpro(Ab,n)
    x=zeros(n,1);
    x(1)=Ab(1,n+1)/Ab(1,1);
    for i=2:n
        sum=0;
        for p=1:i-1
            sum=sum+Ab(i,p)*x(p);
        end
        x(i)=(Ab(i,n+1)-sum)/Ab(i,i);
    end
    
end