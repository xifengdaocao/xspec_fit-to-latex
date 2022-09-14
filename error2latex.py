import math

def error_repro(error):
    
    if error>0.0001 or error<100:
        error_new = format(error, '.2g')
        flag = 0
    else:
        error_new = format(error, '.2e')
        flag = 1
    return float(error_new)

def getdeci(error):
    
    if error<10:
        #print(float(error))
        if len(str(error).split('e'))>1:
            length = abs(int(str(error).split('e')[1]))
        else:
            length = len(str(error).split('.')[1])
    else:
        length = 0
    
    return length

def geterror(value, err_low, err_high):
    
    if abs(value)>10000 or abs(value)<0.001:
        value_new = format(value, '.3e')
        power = int(str(value_new).split('e')[1])
        
        #print(power)
        
        value_base = value/math.pow(10, power)
        err_low_base = error_repro(err_low/math.pow(10, power))
        err_high_base = error_repro(err_high/math.pow(10, power))
        
        if math.pow(10, getdeci(err_low_base))*err_low_base>30:
            err_low_base = format(err_low_base, '.1g')
            
        if math.pow(10, getdeci(err_high_base))*err_high_base>30:
            err_high_base = format(err_high_base, '.1g')
        
        deci = max(getdeci(float(err_low_base)), getdeci(float(err_high_base)))
        value_base = format(value_base, f'.{deci}f')
        
        string = f"${value_base}_{{-{err_low_base}}}^{{+{err_high_base}}} \times 10^{{{power}}}$"
    
    elif abs(value)<0.99:
        value_base = value
        err_low_base = error_repro(err_low)
        err_high_base = error_repro(err_high)
        
        if math.pow(10, getdeci(err_low_base))*err_low_base>30:
            err_low_base = format(err_low_base, '.1g')
            
        if math.pow(10, getdeci(err_high_base))*err_high_base>30:
            err_high_base = format(err_high_base, '.1g')
        
        deci = max(getdeci(float(err_low_base)), getdeci(float(err_high_base)))
        value_base = format(value_base, f'.{deci}f')
        
        string = f"${value_base}_{{-{err_low_base}}}^{{+{err_high_base}}}$"   
        
    else:
        value_base = value
        
        if err_low<0.99 or err_high<0.99:
            err_low_base = error_repro(err_low)
            err_high_base = error_repro(err_high)

            if math.pow(10, getdeci(err_low_base))*err_low_base>30:
                err_low_base = format(err_low_base, '.1g')

            if math.pow(10, getdeci(err_high_base))*err_high_base>30:
                err_high_base = format(err_high_base, '.1g')

            deci = max(getdeci(float(err_low_base)), getdeci(float(err_high_base)))
            value_base = format(value_base, f'.{deci}f')

            string = f"${value_base}_{{-{err_low_base}}}^{{+{err_high_base}}}$"  
        else:
            err_low_base = float(format(err_low, ".1f"))
            err_high_base = float(format(err_high, ".1f"))
            
            if math.pow(10, getdeci(err_low_base))*err_low_base>30:
                err_low_base = format(err_low_base, '.0f')

            if math.pow(10, getdeci(err_high_base))*err_high_base>30:
                err_high_base = format(err_high_base, '.0f')

            deci = max(getdeci(float(err_low_base)), getdeci(float(err_high_base)))
            value_base = format(value_base, f'.{deci}f')

            string = f"${value_base}_{{-{err_low_base}}}^{{+{err_high_base}}}$"  
    
    return string, value_base, err_low_base, err_high_base

def get_xspec_error(value, low_value, high_value):
    
#     if float(value)<0:
#         a = low_value
#         b = high_value
        
#         low_value = str(abs(float(b)))
#         high_value = str(abs(float(a)))
        
        
    
    value = float(value)
    
    #value = abs(float(value))

    err_low = value-float(low_value)
    err_high = float(high_value)-value
    
    #value = abs(float(value))
    
    
    if abs(value)>10000 or abs(value)<0.001:
        value_new = format(value, '.3e')
        power = int(str(value_new).split('e')[1])
        
        #print(power)
        
        value_base = value/math.pow(10, power)
        err_low_base = error_repro(err_low/math.pow(10, power))
        err_high_base = error_repro(err_high/math.pow(10, power))
        
        if math.pow(10, getdeci(err_low_base))*err_low_base>30:
            err_low_base = format(err_low_base, '.1g')
            
        if math.pow(10, getdeci(err_high_base))*err_high_base>30:
            err_high_base = format(err_high_base, '.1g')
        
        deci = max(getdeci(float(err_low_base)), getdeci(float(err_high_base)))
        value_base = format(value_base, f'.{deci}f')
        
        string = f"${value_base}_{{-{err_low_base}}}^{{+{err_high_base}}}" +r"\times" +f"10^{{{power}}}$"
    
    elif abs(value)<0.99:
        value_base = value
        err_low_base = error_repro(err_low)
        err_high_base = error_repro(err_high)
        
        if math.pow(10, getdeci(err_low_base))*err_low_base>30:
            err_low_base = format(err_low_base, '.1g')
            
        if math.pow(10, getdeci(err_high_base))*err_high_base>30:
            err_high_base = format(err_high_base, '.1g')
        
        deci = max(getdeci(float(err_low_base)), getdeci(float(err_high_base)))
        value_base = format(value_base, f'.{deci}f')
        
        if low_value=='0':
            err_low_base = 'P'
        if high_value=='0':
            err_high_base = 'P'
        
        string = f"${value_base}_{{-{err_low_base}}}^{{+{err_high_base}}}$"   
        
    else:
        value_base = value
        
        if abs(err_low)<0.99 or abs(err_high)<0.99:
            err_low_base = error_repro(err_low)
            err_high_base = error_repro(err_high)

            if math.pow(10, getdeci(err_low_base))*err_low_base>30:
                err_low_base = format(err_low_base, '.1g')

            if math.pow(10, getdeci(err_high_base))*err_high_base>30:
                err_high_base = format(err_high_base, '.1g')

            deci = max(getdeci(float(err_low_base)), getdeci(float(err_high_base)))
            value_base = format(value_base, f'.{deci}f')
            
            if low_value=='0':
                err_low_base = 'P'
            if high_value=='0':
                err_high_base = 'P'

            string = f"${value_base}_{{-{err_low_base}}}^{{+{err_high_base}}}$"  
        else:
            err_low_base = float(format(err_low, ".1f"))
            err_high_base = float(format(err_high, ".1f"))
            
            if math.pow(10, getdeci(err_low_base))*err_low_base>30:
                err_low_base = format(err_low_base, '.0f')

            if math.pow(10, getdeci(err_high_base))*err_high_base>30:
                err_high_base = format(err_high_base, '.0f')

            deci = max(getdeci(float(err_low_base)), getdeci(float(err_high_base)))
            value_base = format(value_base, f'.{deci}f')
            
            if low_value=='0':
                err_low_base = 'P'
            if high_value=='0':
                err_high_base = 'P'            
            

            string = f"${value_base}_{{-{err_low_base}}}^{{+{err_high_base}}}$"  
    
    return string, value_base, err_low_base, err_high_base
