import json
import argparse


if __name__ == '__main__':
    # Arguments
    p = argparse.ArgumentParser(description="Look for Saved Snapchat Messages")
    p.add_argument("snapusername", help="My Snapchat username")
    p.add_argument("targetsnapusername", help="The Snapchat username of the target")
    p.add_argument("filepath", help='Filepath into the mydata_XXXXXXXX Folder')
    args = p.parse_args()

    # Getting Data
    with open(args.filepath + '/json/chat_history.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Sorting Data to date
    sortedData = []
    for i in data:
        for j in data[i]:
            try:
                if j['From'] == args.targetsnapusername and j['Text'] != '':
                    sortedData.append(j)
            except KeyError:
                pass
            try:
                if j['To'] == args.targetsnapusername and j['Text'] != '':
                    sortedData.append(j)
            except KeyError:
                pass
    newlist = sorted(sortedData, key=lambda d: d['Created'])

    # Writing in file
    with open('Snapchat-' + args.snapusername + '-' + args.targetsnapusername + '.txt', "w", encoding='utf-8') as file:
        for i in newlist:
            try:
                file.write(str(i['From']) + ' [ ' + str(i['Created'][0:-4]) + ' ] : ' + str(i['Text']) + ' \n')
            except KeyError:
                file.write(args.snapusername + ' [ ' + str(i['Created'][0:-4]) + ' ] : ' + str(i['Text']) + ' \n')
