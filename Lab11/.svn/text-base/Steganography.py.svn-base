import numpy,zlib,base64,re,copy
class Payload:
    def __init__(self, img=None, compressionLevel=-1,xml=None):
        if img is None and xml is None:
            raise ValueError("Both img and xml are not provided")
        self.xml=xml
        self.img=img

        if (self.img is not None):
            if type(self.img) is not numpy.ndarray:
                raise TypeError("Incorrect input type")

            self.xml=self.generateXML_header(compressionLevel)
            xml_content=self.convert_img2str()
            if compressionLevel == -1:
                self.xml+=base64.b64encode(xml_content).decode()+"\n"+"</payload>"
            elif compressionLevel >= 0 and compressionLevel <=9:
                xml_content=zlib.compress(xml_content,compressionLevel)
                self.xml+=base64.b64encode(xml_content).decode()+"\n"+"</payload>"
            else:
                raise ValueError("Incorrect compressionLevel value")


        elif(self.xml is not None):
            if type(self.xml) is not str:
                raise TypeError("Incorrect input type")
            self.read_xml()


    def generateXML_header(self,compressionLevel):
        header='<?xml version="1.0" encoding="UTF-8"?>'
        if len(self.img.shape) == 3:
            type='"Color"'
        else:
            type='"Gray"'
        size='"'+str(self.img.shape[0])+","+str(self.img.shape[1])+'"'
        if compressionLevel == -1:
            compress='"False"'
        else:
            compress='"True"'
        header+="\n"+"<payload type="+type+" size="+size+" compressed="+compress+">"+"\n"
        return header

    def convert_img2str(self):
        arr=bytearray()
        if(len(self.img.shape)==3):
            colors=self.img.shape[2]
            i=colors
            while i>0:
                for row in self.img:
                    for column in row:
                        arr.extend(column[colors-i])
                i-=1
        else:
            for row in self.img:
                for column in row:
                    arr.extend(column)
        return arr
    def convert_str2img(self,xml,color):
        cnt=0
        if(color=="Color"):
            i=3
            while i>0:
                for row in self.img:
                    for column in row:
                        column[3-i]=xml[cnt]
                        cnt+=1
                i-=1

        else:
            for row in self.img:
                i=0
                while i<self.img.shape[1]:
                    row[i]=xml[cnt]
                    cnt+=1
                    i+=1

    def read_xml(self):
        type=re.search(r'type=\"(\w+)\"',self.xml).group(1)
        size=re.search(r'size="(\d+)\,(\d+)"',self.xml)
        rows=int(size.group(1))
        columns=int(size.group(2))
        compressed=re.search(r'compressed="(\w+)"',self.xml).group(1)
        xml=self.xml.split("\n")[2]
        xml_decoded=base64.b64decode(xml.encode())
        if compressed == "True":
            xml_decompressed=zlib.decompress(xml_decoded)
        else:
            xml_decompressed=xml_decoded
        if type == "Gray":
            self.img=numpy.ndarray(shape=(rows,columns),dtype=numpy.uint8)
        else:
            self.img=numpy.ndarray(shape=(rows,columns,3),dtype=numpy.uint8)
        self.convert_str2img(xml_decompressed,type)


class Carrier:
    def __init__(self,img):
        if type(img) is not numpy.ndarray:
            raise TypeError("Incorrect input type")
        self.img=img

    def payloadExists(self):
        payload_buff=[]
        nb=7
        if(len(self.img.shape)==3):
            i=3
            while i>0:
                for row in self.img:
                    for column in row:
                        if nb >= 0:
                            if column[3-i]&numpy.uint8(1) == 1:
                                payload_buff.append(1)
                            else:
                                payload_buff.append(0)
                            nb-=1
                        else:
                            if chr(numpy.packbits(payload_buff)[0]) == "<":
                                return True
                            else:
                                return False
                i-=1
        else:
            for row in self.img:
                i=0
                while i<self.img.shape[1]:
                    if nb >= 0:
                        if row[i]&numpy.uint8(1) ==1:
                            payload_buff.append(1)
                        else:
                            payload_buff.append(0)
                        nb-=1
                    else:
                        if chr(numpy.packbits(payload_buff)[0]) == "<":
                            return True
                        else:
                            return False
                    i+=1

    def clean(self):
        image=copy.deepcopy(self.img)
        clean_matrix=numpy.ndarray(shape=image.shape,dtype=numpy.uint8)
        clean_matrix.fill(254)
        numpy.bitwise_and(clean_matrix,image,image)
        return image

    def embedPayload(self,payload,override=False):

        if type(payload) is not Payload:
            raise TypeError("Incorrect input type")
        if len(payload.img.shape)==3:
            color=3
        else:
            color=1
        payload_size=8*payload.img.shape[0]*payload.img.shape[1]*color
        if len(self.img.shape)==3:
            color1=3
        else:
            color1=1
        carrier_size=self.img.shape[0]*self.img.shape[1]
        if payload_size>carrier_size*color1:
            raise ValueError("Carrier can not hold payload")
        if self.payloadExists()==True and override ==False:
            raise Exception("Payload exist and can not override")

        xml_list=numpy.ndarray(shape=(len(payload.xml),1),dtype=numpy.uint8)
        cnt=0
        for item in payload.xml:
            xml_list[cnt][0]=ord(item)
            cnt+=1
        xml_binary=numpy.unpackbits(xml_list)
        image=copy.deepcopy(self.img)
        if color1==3:
            reshaped_image=image.flatten()
            ordered_image=numpy.concatenate((reshaped_image[0::3],reshaped_image[1::3],reshaped_image[2::3]))
            embed_image=ordered_image[:len(xml_binary)]
        else:
            ordered_image=image.flatten()
            embed_image=ordered_image[:len(xml_binary)]

        clean_matrix=numpy.ndarray(shape=embed_image.shape,dtype=numpy.uint8)
        clean_matrix.fill(254)
        numpy.bitwise_and(clean_matrix,embed_image,embed_image)
        numpy.bitwise_or(embed_image,xml_binary,embed_image)
        reshaped_image=numpy.concatenate((embed_image,ordered_image[len(xml_binary):]))

        if color1==3:
            reshaped_image=reshaped_image.reshape(3,-1)
            reshaped_image=numpy.dstack(tuple(reshaped_image))
            image=reshaped_image.reshape(image.shape)
        else:
            image=reshaped_image.reshape(image.shape)


        return image



    def extractPayload(self):
        if self.payloadExists()== False:
            raise Exception("Payload not exist")
        xml_list=[]

        image=copy.deepcopy(self.img)
        if len(image.shape)==3:
            reshaped_image=image.flatten()
            ordered_image=numpy.concatenate((reshaped_image[0::3],reshaped_image[1::3],reshaped_image[2::3]))
        else:
            ordered_image=image.flatten()

        clean_matrix=numpy.ndarray(shape=ordered_image.shape,dtype=numpy.uint8)
        clean_matrix.fill(1)
        xml_list=numpy.bitwise_and(clean_matrix,ordered_image)
        xml_packed=numpy.packbits(xml_list)
        xml=""
        cnt=0

        for item in xml_packed:
            xml+=chr(item)
            if chr(item)==">":
                cnt+=1
            if cnt==3:
                break


        payload=Payload(None,-1,xml)
        return payload





