import logging


def normalise(matrix):
    return [[x - 1 for x in row] for row in matrix]


def validate(matrix):
    """
    matrix is NxN,
    Contains only integers
    Integers are in range(1, N)
    No duplicate integers are found in row

    :param matrix:
    :return:
    """
    # check if matrix is square
    N = len(matrix)
    for i in range(N):
        if len(matrix[i]) != N:
            logging.error('Validation error, matrix is not square')
            return False
        if len(matrix[i]) != len(set(matrix[i])):
            logging.error('Validation error, matrix row contains duplicates')
            return False
        for j in range(N):
            x = matrix[i][j]
            # check if matrix contains only integers
            if type(x) != int:
                logging.error('Validation error, matrix contains not integers')
                return False
            # check if matrix integers are in valid range
            if x < 1 or x > N:
                print(x, N)
                logging.error('Validation error, matrix contains items in invalid range')
                return False
    return True


def apartment_prefers_applicant_over_tenant(apartments, apartment, tenant, applicant):
    apartment_preferences = apartments[apartment]
    logging.debug('Apartment {}, tenant {}, applicant {}'.format(apartment, tenant, applicant))
    if apartment_preferences.index(applicant) < apartment_preferences.index(tenant):
        return True
    else:
        return False


def near_perfect_matches(applicants, apartments):
    # validate matrices
    for matrix in [applicants, apartments]:
        if not validate(matrix=matrix):
            logging.error('Matrix Validation Error')
            return

    # normalise matrices
    applicants = normalise(applicants)
    apartments = normalise(apartments)

    if len(applicants) != len(apartments):
        logging.error('Matrices have different dimension')
        return

    N = len(applicants)
    tenants = [-1 for _ in range(N)]
    free_applicants = [True for _ in range(N)]
    free_applicants_count = N

    while free_applicants_count:
        logging.debug('Free applicants count ', free_applicants_count)
        # pick the first free applicant
        applicant = 0
        for i in range(N):
            if free_applicants[i]:
                applicant = i
                break
            else:
                continue
        logging.debug('Applicant', applicant)
        # go over applicant preferences
        for j in range(N):
            logging.debug(j)
            if free_applicants[applicant] is False:
                break
            apartment = applicants[applicant][j]
            logging.debug('Apartment', apartment)
            # if apartment of preference is free there is a connection
            # which can be broken if apartment prefers someone else later in
            # process
            tenant = tenants[apartment]
            logging.debug('Tenant', tenant)
            if tenant == -1:
                tenants[apartment] = applicant
                free_applicants[applicant] = False
                free_applicants_count -= 1
            else:
                # if apartment of preference is not free
                # check apartment preference
                if apartment_prefers_applicant_over_tenant(
                        apartments,
                        apartment=apartment,
                        tenant=tenant,
                        applicant=applicant) is True:
                    tenants[apartment] = applicant
                    free_applicants[applicant] = False
                    free_applicants[tenant] = True
    logging.info('Near perfect match', tenants)
    return [tenant + 1 for tenant in tenants]
