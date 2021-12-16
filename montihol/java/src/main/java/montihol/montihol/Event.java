package montihol.montihol;

import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.Action;
import org.bukkit.event.inventory.InventoryClickEvent;
import org.bukkit.event.player.PlayerInteractEvent;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class Event implements Listener {
    Player p;
    int setans;
    List<Integer> a = Arrays.asList(1, 4, 7);

    @EventHandler
    public void PlayerInteractEvent(PlayerInteractEvent e) {
        if (e.getAction() == Action.RIGHT_CLICK_AIR || e.getAction() == Action.RIGHT_CLICK_BLOCK) {
            p = e.getPlayer();
            ItemStack i = e.getItem();
            if (i.getType() == Material.NETHER_STAR) {
                new montiholGui().gui(p);
                Collections.shuffle(a);
                setans = a.get(0);
            }
        }
    }

    int i1 = -1;
    int state = 0;

    @EventHandler
    public void onInventoryClick(InventoryClickEvent e) {   //인벤토리 클릭 시
        Inventory inven = e.getInventory();
        if (inven.getSize() == 18) {
            if(state == 1) {
                i1 = -1;
            }

            int i = e.getSlot();

            if (i == 1 || i == 4 || i == 7) {
                i1 = i;
            }

            e.setCancelled(true);
            if (state == 0) {
                ItemStack item1, item2, item3;
                item1 = new ItemStack(Material.OAK_SIGN);
                ItemMeta meta = item1.getItemMeta();
                meta.setDisplayName("알리미");
                meta.setLore(Arrays.asList("선택을 유지할까요?", "다시 선택시 첫번째 선택은 금지됩니다"));
                item1.setItemMeta(meta);
                item2 = new ItemStack(Material.BLUE_STAINED_GLASS_PANE);
                meta = item2.getItemMeta();
                meta.setDisplayName("네");
                item2.setItemMeta(meta);
                item3 = new ItemStack(Material.RED_STAINED_GLASS_PANE);
                meta = item3.getItemMeta();
                meta.setDisplayName("아니요");
                item3.setItemMeta(meta);
                inven.setItem(12, item2);
                inven.setItem(13, item1);
                inven.setItem(14, item3);

                if (i == 12) {
                    if (i == setans) {
                        p.sendMessage("당첨");

                    } else {
                        p.sendMessage("실패..");
                    }

                    p.closeInventory();
                    state = 0;
                    return;
                } else if (i == 14) {
                    double h = Math.abs(Math.random() * 10);
                    if(h <= 50){
                        inven.setItem(a.get(1), new ItemStack(Material.AIR));
                    }else {
                        inven.setItem(a.get(2), new ItemStack(Material.AIR));
                    }

                        state = 1;
                    return;
                } else if(i>=9){
                    p.sendMessage("선택지를 클릭하세요");
                    return;
                }
            } else if (state == 1) {
                if (i == setans) {
                    p.sendMessage("당첨");
                } else {
                    p.sendMessage("실패..");

                }
                p.closeInventory();
                state = 0;
                return;
            }
        }

    }
}


