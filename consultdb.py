import simplejson
import sqlite3 as lite

def generateJSON():
	con = lite.connect('havas.db')
	datadict = []

	with con:
		cur = con.cursor()
		schema = cur.execute("SELECT campaign, ROUND(avg(CR), 2) cr_avg FROM Media group by campaign order by cr_avg desc")
		for x in schema.fetchall():
			media = {
			'campaign' : x[0],
			'cr_avg' : x[1]
			}
			datadict.append(media)
			
	out_file = open("media.json",'w')
	simplejson.dump(datadict,out_file, indent=4)    
	out_file.close()

def main():

	consultdb()




if __name__ == '__main__':
    main()
"""		for x in schema.fetchall():
			media = {
			'id' : x[0],
			'date': x[1],
			'campaign' : x[2],
			'product' : x[3],
			'placement' : x[4],
			'creative' : x[5],           
			'clicks' : x[6],
			'impressions' : x[7],
			'sales' : x[8],
			'cost' : x[9],           
			'CTR' : x[10],
			'CR' : x[11],
			'CPA' : x[12]}
			datadict.append(media)
"""