from pysqlc import DB

class DataGetter:
    """
    Simple class to get data for ridings and candiates stored in 
    the `canfedelxn19` database
    """

    def __init__(self):
        self.db = DB(db_env='prod', database="canfedelxn19")

    def get_ridings(self):
        """
        simple functino to get a list of all ridings and their names
        """
        q = "SELECT riding_id, riding_name_en FROM elxn_ridings;"
        data = self.db.query(q)
        ridings = {}
        for each in data:
            ridings[each[0]] = each[1]
        return ridings


    def get_riding_info(self, riding_id):
        """
        function to get a bunch of info about a riding
        """
        q = """
        SELECT 
            riding_id,
            riding_name_en,
            riding_pop,
            riding_median_house_income,
            riding_encumbent,
            riding_prov
        FROM elxn_ridings
            WHERE riding_id={};
        """.format(riding_id)
        try:
            data = self.db.query(q, q_type="SELECT")
            print(data)
            return {
                "riding_id": data[0][0],
                "riding_name_en": data[0][1],
                "riding_population": data[0][2]
            }
        except Exception as e:
            return {"error":"Error in the query: {}".format(e)}


    def get_riding_candidates(self, riding_id):
        """
        simple API to get the candiates of a specific riding...
        """
        q = """
        SELECT 
            candidate_name,
            party_name
        FROM elxn_candidates
            WHERE riding_id = {}
        """.format(riding_id)
        try:
            return {each[1]:each[0] for each in self.db.query(q)}
        except Exception as e:
            return {"error":"Error in the query: {}".format(e)}

if __name__ == "__main__":
    print("starting...")
    DG = DataGetter()
    print(DG.get_ridings())
    