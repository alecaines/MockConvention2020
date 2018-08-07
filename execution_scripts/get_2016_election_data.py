import sys
import csv

def main():
    if len(sys.argv) < 3:
        print("USAGE: get_2016_election_data.py <DataFile> <OutputFile> <State>")
    else:
        dataFile = sys.argv[1]
        outputFile = sys.argv[2]
        state = sys.argv[3]

        state_index = 0
        county_index = 0
        rep_votes_index = 0
        dem_votes_index = 0
        ind_votes_index = 0
        total_votes_index = 0
        vote_direction = None

        dataList = []
        outputList = []

        with open(dataFile, "r") as openFile:
            reader = csv.reader(openFile, delimiter=',')
            for line in reader:
                print(line)
                data = line[0].split(";")
                for item in line[1].split(";")[1:]:
                    data.append(item)
                dataList.append(data)

        openFile.close()

        for index in range(len(dataList[0])):
            if dataList[0][index] == "State":
                state_index = index
                print(state_index)
            elif dataList[0][index] == "County":
                county_index = index
                print(county_index)
            elif dataList[0][index] == "Republicans 2016":
                rep_votes_index = index
                print(rep_votes_index)
            elif dataList[0][index] == "Democrats 2016":
                dem_votes_index = index
                print(dem_votes_index)
            elif dataList[0][index] == "Libertarians 2016":
                ind_votes_index = index
                print(ind_votes_index)
            elif dataList[0][index] == "Votes":
                total_votes_index = index
                print(total_votes_index)

        for county in dataList[1:]:
            print(county)
            print(len(county))
            if county[rep_votes_index] > county[dem_votes_index]:
                vote_direction = "REP"
            else:
                vote_direction = "DEM"
            outputList.append([county[state_index], county[county_index],
                               county[rep_votes_index], county[dem_votes_index], county[ind_votes_index],
                               county[total_votes_index], vote_direction])

            #set the value of the REP votes to vote count
            if outputList[-1][5] is not "" and outputList[-1][2] is not "":
                outputList[-1][2] = round(float(outputList[-1][5]) * (float(outputList[-1][2]) / 100))

            #set the value of the DEM votes to vote count
            if outputList[-1][5] is not "" and outputList[-1][3] is not "":
                outputList[-1][3] = round(float(outputList[-1][5]) * (float(outputList[-1][3]) / 100))

            #set the value of the IND votes to vote count
            if outputList[-1][5] is not "" and outputList[-1][4] is not "":
                outputList[-1][4] = round(float(outputList[-1][5]) * (float(outputList[-1][4]) / 100))


        csv_header = ["State", "County", "REP votes", "DEM votes", "IND votes", "Total votes", "REP/DEM"]
        with open(outputFile, "w") as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerow(csv_header)
            for county in outputList:
                if county[0] == state.replace("_", " "):
                    writer.writerow(county)

        outfile.close()

if __name__ == "__main__":
    main()