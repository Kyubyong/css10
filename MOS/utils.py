import numpy as np

def remove_outliers(Z):
    """ Removes outlying scores by setting them to NaN

    Z: a matrix of scores, where the rows are subjects and columns are sentences
    """
    N,M = Z.shape

    print('Started with %d workers and %d scores.\n'%(np.size(Z,0),np.sum(~np.isnan(Z))))

    mu = np.nanmean(Z) # MOS for each sentence
    s = np.nanstd(Z)   # std dev for each sentence

    mu_norm = abs(Z-mu)/s # normalized scores
    outlying_scores = (mu_norm > 3.0)
    outlying_workers = np.sum(outlying_score,1) > .05*np.sum(~np.isnan(Z),1)

    Z[outlying_score] = np.NaN # remove outlying scores (greater than 2.5 std devs away from the mean)
    Z = Z[~outlying_workers] # remove subjects who have more than 5% of outlying scores

    print('Removed %d outlying scores.\n'%np.sum(outlying_scores))
    print('Removed %d outlying workers.\n'%np.sum(outlying_workers))

    print('Finished with %d workers and %d scores.\n\n'%(np.size(Z,0), np.sum(~np.isnan(Z))))

    return Z

def zscore(Z):
    """Returns 1-100 scores.

    This procedures:
       1. Centers each worker's scores at 0.
       2. Normalizes each worker's variance to 1.0.
       3. Stretches the scores to a 1-100 scale.

    Z: a matrix of scores, where the rows are subjects and columns are sentences
    """
    eps = 1e-8

    nsubjects  = np.size(Z,0)
    nsentences = np.size(Z,1)

    for i in range(nsubjects):
        mos = np.nanmean(Z[i,:])
        std = np.nanstd(Z[i,:])
        Z[i,:] = (Z[i,:] - mos) / (std + eps)
        Z[i,:] =  Z[i,:] + 3.5

    return Z

# (TODO Tommy): Check to make sure this is correct.  The orignal code looks like it handles
# multiple cases so I simplified it.
def mos_variance(Z):
    """Determines the variance of the mean opinion score, given a matrix of scores.
     Unknown scores are represented by NaN.

     Z: a N-by-M matrix of scores, where the rows are subjects and columns are sentences
     We assume that

       Z_ij = mu + x_i + y_j + eps_ij, where

     mu is the mean opinion score (given by nanmean(Z(:)))
     x_i ~ N(0, sigma_w^2), with sigma_w^2 modeling worker variation
     y_j ~ N(0, sigma_s^2), with sigma_y^2 modeling sentence variation
     eps_ij ~ N(0, sigma_u^2), with sigma_u^2 modeling worker uncertainty

     The returned value v_mu is Var[mu].
    """
    def nancount(vec):
        n = np.sum(~np.isnan(vec))
        return n

    def vertical_var(Z):
        rows,cols = np.shape(Z)
        v = []
        for i in range(cols):
            if nancount(Z[:,i]) >= 2: #make sure enough samples for variance
                v.append(np.nanvar(Z[:,i]))
        v = np.array(v)
        return np.mean(v)

    N, M = np.shape(Z)

    W  = ~np.isnan(Z)
    Mi = np.sum(W,0)
    Nj = np.sum(W,1)
    T = np.sum(W)

    v_wu = vertical_var(Z)
    v_su = vertical_var(Z.T)
    v_swu = np.nanvar(Z)

    v_s = v_swu - v_wu
    v_w = v_swu - v_su
    v_u = (v_swu-v_s-v_w)

    v_mu = v_w*np.sum(Nj**2)/T**2 + v_s*np.sum(Mi**2)/T**2 + v_u/T 
    v_mu

    return v_mu

def corrcoef(u,v):
    N = len(u)
    
    u = u - np.nanmean(u)
    v = v - np.nanmean(v)
    
    c = (np.nansum(u * v)/(N-1))/(np.nanstd(u) * np.nanstd(v))
    
    return c

def compute_mos_ci95_3gaussian(Z):
    """
    Computes the MOS and 95% confidence interval for the mean, using a sum of 3
    Gaussians model.
    
    TODO: Normalize scores? 
    """
    from scipy import stats
    t = stats.t.ppf(.5*(1+.95), np.min(np.shape(Z)))
    #t = 1.96
    
    mos = np.nanmean(Z)
    ci95 = t*np.sqrt(mos_variance(Z))
    
    return mos,ci95

