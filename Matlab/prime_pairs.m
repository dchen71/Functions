%Returns the smallest prime number p smaller than 100,000 such
%that (p + n) is also prime, where n is a scalar integer and is the sole input argument to the function. If no
%such number exists, then the function returns -1.

function lowest =  prime_pairs(n)
    lowest = -1;
    primeList = primes(100000);

    for idx = 1:numel(primeList)
        if isprime(primeList(idx) + n)
            lowest = primeList(idx);
            break;
        end
    end
    
end