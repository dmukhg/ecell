def FooterFormatter(qs):
        foot = qs.filter(parent=None)
        sub_foot=[]
        for item in foot:
            sub_foot.append(qs.filter(parent=item))
        result = (foot,sub_foot)
        return result
