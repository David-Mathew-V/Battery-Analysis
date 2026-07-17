# sql_queries.py

def del_V():

    return """
        SELECT
            SampleID,
            dev_unit_chl,
            test_id,
            experiment_order,
            cycle_id,
            seq_id,
            step_type,
            voltage,
            current
        FROM record
        WHERE SampleID IN({placeholders})
        ORDER BY
            SampleID ASC,
            experiment_order ASC,
            CAST(seq_id AS UNSIGNED) ASC;
    """

def check_form_exist():
    return """
        SELECT sampleId
        FROM record
        GROUP BY sampleId
        HAVING
            SUM(CASE WHEN experiment_order = 1 THEN 1 ELSE 0 END) > 0
            AND
            SUM(
                CASE
                    WHEN experiment_order = 1
                        AND cycle_type NOT IN ('rest', 'cc_chrg', 'cccv_chrg')
                    THEN 1
                    ELSE 0
                END
            ) = 0;
    """

# Query registry
QUERIES = {
    "delta_V": del_V,
    "check_formation_cycle": check_form_exist,
    
}